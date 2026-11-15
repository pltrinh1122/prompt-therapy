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
