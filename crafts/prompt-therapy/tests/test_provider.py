"""provider.py: the fake adapter is deterministic, offline, and says it is not therapy first."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import provider


class FakeProviderTests(unittest.TestCase):
    def test_greet_opens_with_the_not_therapy_line(self):
        self.assertTrue(provider.FakeProvider().reply("greet", {}).startswith(provider.NOT_THERAPY))

    def test_context_fills_and_missing_keys_read_empty(self):
        p = provider.FakeProvider()
        self.assertIn("x y", p.reply("describe", {"summary": "x y"}))
        self.assertNotIn("{", p.reply("describe", {}))

    def test_replies_are_bounded(self):
        self.assertLessEqual(len(provider.FakeProvider().reply("helps", {"helps": "z" * 5000})), provider.MAX_CHARS)


if __name__ == "__main__":
    unittest.main()


def _r(text, stop="end_turn"):
    return {"content": [{"type": "text", "text": text}], "stop_reason": stop, "usage": {"input_tokens": 100, "output_tokens": 20}}

class _Post:
    """A recorded Messages endpoint: returns the given responses in turn and records each request body."""
    def __init__(self, *responses): self.responses, self.calls = list(responses), []
    def __call__(self, body):
        self.calls.append(body)
        r = self.responses.pop(0)
        if isinstance(r, Exception): raise r
        return r


class AnthropicProviderTests(unittest.TestCase):
    """d-work #3: the model writes only the framing; the exact parts survive a model that drops them."""
    def test_the_greeting_always_opens_with_the_no_therapy_line(self):
        p = provider.AnthropicProvider("claude-haiku-5-5", post=_Post(_r("Hello there! What happened?")))
        self.assertTrue(p.reply("greet", {}).startswith(provider.NOT_THERAPY))
        self.assertEqual(p.usage, [(100, 20)])

    def test_options_and_yes_no_are_added_whatever_the_model_writes(self):
        p = provider.AnthropicProvider("m", post=_Post(_r("Which of these fits?"), _r("May I keep it?")))
        self.assertTrue(p.reply("match", {"options": "1. a\n2. None of these."}).endswith("1. a\n2. None of these."))
        self.assertTrue(p.reply("consent", {}).endswith("(yes / no)"))

    def test_a_refusal_an_error_or_an_empty_reply_falls_back_to_the_template(self):
        p = provider.AnthropicProvider("m", post=_Post(_r(""), _r("no", "refusal"), RuntimeError("down")))
        for _ in range(3):
            self.assertEqual(p.reply("greet", {}), provider.FakeProvider().reply("greet", {}))
        self.assertEqual(p.fallbacks, 3)

    def test_the_request_carries_the_system_rules_and_a_bound(self):
        post = _Post(_r("Thanks."))
        provider.AnthropicProvider("claude-haiku-5-5", effort="low", post=post).reply("close", {"kept": "Nothing was kept."})
        body = post.calls[0]
        self.assertEqual((body["model"], body["system"], body["output_config"]), ("claude-haiku-5-5", provider.SYSTEM, {"effort": "low"}))
        self.assertLessEqual(body["max_tokens"], 2048)

    def test_no_credential_refuses_before_any_request(self):
        import os, unittest.mock
        with unittest.mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": "", "ANTHROPIC_AUTH_TOKEN": ""}):
            with self.assertRaises(RuntimeError):
                provider.AnthropicProvider("m")

    def test_auth_headers_follow_dmc_provider_auth(self):
        """Sign-in: a Bearer token with the OAuth beta header, preferred over a key; else the key; else refused."""
        h = provider.auth_headers({"ANTHROPIC_AUTH_TOKEN": "tok", "ANTHROPIC_API_KEY": "key"})
        self.assertEqual(h, {"authorization": "Bearer tok", "anthropic-beta": provider.OAUTH_BETA})
        self.assertEqual(provider.auth_headers({"ANTHROPIC_API_KEY": "key"}), {"x-api-key": "key"})
        with self.assertRaises(RuntimeError):
            provider.auth_headers({})

    def test_compose_keeps_the_anchor_and_what_was_kept(self):
        self.assertIn("I answer for the result.", provider.compose("anchor", "It seems to lead here.", {"anchor": "I answer for the result."}))
        self.assertTrue(provider.compose("close", "Thank you.", {"kept": "Nothing was kept."}).endswith("Nothing was kept."))
