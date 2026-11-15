"""evaluate.py: the cost at the dated prices, the spend bound, and the same judgement as the adversarial test (d-work #3)."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evaluate, provider

class CostTests(unittest.TestCase):
    def test_cost_at_the_dated_prices(self):
        self.assertAlmostEqual(evaluate.cost("claude-haiku-5-5", [(1_000_000, 1_000_000)]), 0.60)
        self.assertAlmostEqual(evaluate.cost("claude-opus-5-5", [(500_000, 100_000)]), 4.0)
        self.assertEqual(evaluate.cost("fake", [(10, 10)]), 0.0)

    def test_every_candidate_is_priced(self):
        self.assertEqual(set(evaluate.PRICES), {"claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"})


class _Spender(provider.FakeProvider):
    """Spends a million input tokens a call, so the bound is met on the first member."""
    def __init__(self): self.usage = []
    def reply(self, state, context):
        self.usage.append((1_000_000, 0))
        return super().reply(state, context)


@unittest.skipIf(evaluate.checkout() is None, "evaluate: no dyad-system checkout; skipped")
class RunTests(unittest.TestCase):
    def test_the_fake_provider_passes_every_member(self):
        lines = []
        passed, failed, total = evaluate.run(provider.FakeProvider(), "fake", evaluate.checkout(), 10.0, lines.append)
        self.assertEqual((passed, failed, total), (42, 0, 0.0))

    def test_the_bound_stops_the_run(self):
        lines = []
        passed, failed, total = evaluate.run(_Spender(), "claude-haiku-5-5", evaluate.checkout(), 0.05, lines.append)
        self.assertTrue(any(l.startswith("stop  budget reached") for l in lines))
        self.assertGreaterEqual(failed, 1)
        self.assertLess(passed, 42)


if __name__ == "__main__":
    unittest.main()
