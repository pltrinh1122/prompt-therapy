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


class _Block:
    def __init__(self, text): self.type, self.text = "text", text

class _Response:
    def __init__(self, text, stop="end_turn"):
        self.content, self.stop_reason = [_Block(text)], stop
        self.usage = type("U", (), {"input_tokens": 100, "output_tokens": 20})()

class _Client:
    """A recorded Messages client: returns the given texts in turn and records each request."""
    def __init__(self, *responses): self.responses, self.calls = list(responses), []
    @property
    def messages(self): return self
    def create(self, **kw):
        self.calls.append(kw)
        r = self.responses.pop(0)
        if isinstance(r, Exception): raise r
        return r


class AnthropicProviderTests(unittest.TestCase):
    """d-work #3: the model writes only the framing; the exact parts survive a model that drops them."""
    def test_the_greeting_always_opens_with_the_no_therapy_line(self):
        p = provider.AnthropicProvider("claude-haiku-5-5", client=_Client(_Response("Hello there! What happened?")))
        self.assertTrue(p.reply("greet", {}).startswith(provider.NOT_THERAPY))
        self.assertEqual(p.usage, [(100, 20)])

    def test_options_and_yes_no_are_added_whatever_the_model_writes(self):
        p = provider.AnthropicProvider("m", client=_Client(_Response("Which of these fits?"), _Response("May I keep it?")))
        self.assertTrue(p.reply("match", {"options": "1. a\n2. None of these."}).endswith("1. a\n2. None of these."))
        self.assertTrue(p.reply("consent", {}).endswith("(yes / no)"))

    def test_a_refusal_an_error_or_an_empty_reply_falls_back_to_the_template(self):
        c = _Client(_Response("", "end_turn"), _Response("no", "refusal"), RuntimeError("down"))
        p = provider.AnthropicProvider("m", client=c)
        for _ in range(3):
            self.assertEqual(p.reply("greet", {}), provider.FakeProvider().reply("greet", {}))
        self.assertEqual(p.fallbacks, 3)

    def test_the_request_carries_the_system_rules_and_a_bound(self):
        c = _Client(_Response("Thanks."))
        provider.AnthropicProvider("claude-haiku-5-5", effort="low", client=c).reply("close", {"kept": "Nothing was kept."})
        kw = c.calls[0]
        self.assertEqual((kw["model"], kw["system"], kw["output_config"]), ("claude-haiku-5-5", provider.SYSTEM, {"effort": "low"}))
        self.assertLessEqual(kw["max_tokens"], 2048)

    def test_compose_keeps_the_anchor_and_what_was_kept(self):
        self.assertIn("I answer for the result.", provider.compose("anchor", "It seems to lead here.", {"anchor": "I answer for the result."}))
        self.assertTrue(provider.compose("close", "Thank you.", {"kept": "Nothing was kept."}).endswith("Nothing was kept."))
