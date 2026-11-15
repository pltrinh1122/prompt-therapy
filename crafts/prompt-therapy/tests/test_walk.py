"""walk.py: the engine's states, the three never-rules, and the whole-conversation harness (docs/architecture.md,
Tests). Every conversation under tests/fixtures/conversations runs offline against the fake provider and the
synthetic canon; a walk fails if it diagnoses, says back a name the user wrote, or keeps anything without a yes."""
import json, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import canon, provider, store, walk

HERE = Path(__file__).resolve().parent
CANON = canon.load(HERE / "fixtures" / "canon")
CONVERSATIONS = sorted((HERE / "fixtures" / "conversations").glob("*.json"))


def run(spec: dict):
    s = store.MemoryStore()
    w = walk.Walk(CANON, provider.FakeProvider(), s)
    said = [w.start()]
    states = []
    for turn in spec["turns"]:
        said.append(w.receive(turn))
        states.append(w.state)
    return w, s, said, states


class HarnessTests(unittest.TestCase):
    def test_there_are_conversations(self):
        self.assertGreaterEqual(len(CONVERSATIONS), 4)

    def test_every_conversation(self):
        for path in CONVERSATIONS:
            spec = json.loads(path.read_text())
            with self.subTest(spec["name"]):
                w, s, said, states = run(spec)
                self.assertEqual(states, spec["states"])
                self.assertEqual(w.breaches, 0)
                self.assertTrue(said[0].startswith(provider.NOT_THERAPY))
                if spec["anchor"]:
                    self.assertEqual(w.trail[-1], spec["anchor"])
                    self.assertEqual(CANON.trees[w.tree][w.trail[-1]].kind, "anchor")
                self.assertEqual(bool(s.kept), spec["kept"])
                if spec["kept"]:
                    self.assertEqual(s.kept[w.cid]["canon"], spec["canon"])
                for line in said:
                    self.assertIsNone(walk.DIAGNOSIS.search(line))
                    for name in w.names:
                        self.assertNotIn(name, line)
                self.assertNotIn(w.cid, s.turns)  if states[-1] == "close" else None


class NeverRuleTests(unittest.TestCase):
    def test_a_diagnosis_is_replaced_and_counted(self):
        class Diagnoser(provider.FakeProvider):
            def reply(self, state, context):
                return "The cause is that you trusted it."
        w = walk.Walk(CANON, Diagnoser(), store.MemoryStore())
        self.assertEqual(w.start(), walk.SAFE)
        self.assertEqual(w.breaches, 1)

    def test_a_name_the_user_wrote_is_never_said_back(self):
        class Echo(provider.FakeProvider):
            def reply(self, state, context):
                return "You mentioned Dana."
        w = walk.Walk(CANON, Echo(), store.MemoryStore())
        w.start()
        self.assertEqual(w.receive("It lied to me and Dana saw it"), walk.SAFE)

    def test_redact_hides_names_and_addresses(self):
        self.assertEqual(walk.redact("It told Sam and x@y.org a lie"), "It told [someone] and [someone] a lie")

    def test_causes_are_offered_as_questions(self):
        w = walk.Walk(CANON, provider.FakeProvider(), store.MemoryStore())
        w.start(); w.receive("It stated something false as if it were true"); w.receive("yes")
        text = w.receive("1")
        self.assertIn("Could it be that", text)

    def test_nothing_is_kept_without_yes(self):
        s = store.MemoryStore()
        w = walk.Walk(CANON, provider.FakeProvider(), s)
        w.start()
        for t in ["It stated something false as if it were true", "yes", "1", "1", "yes", "maybe"]:
            w.receive(t)
        self.assertEqual(s.kept, {})


if __name__ == "__main__":
    unittest.main()
