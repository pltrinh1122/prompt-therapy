"""store.py: turns live for the session; a kept record holds only the consented fields; delete removes all."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import store


class MemoryStoreTests(unittest.TestCase):
    def test_expire_drops_turns_and_keeps_a_consented_record(self):
        s = store.MemoryStore(); c = s.open()
        s.append(c, ("user", "hello")); s.keep(c, {"symptom": "x", "canon": "S1"}); s.expire(c)
        self.assertNotIn(c, s.turns); self.assertEqual(s.kept[c], {"symptom": "x", "canon": "S1"})

    def test_a_kept_record_refuses_a_transcript(self):
        s = store.MemoryStore(); c = s.open()
        with self.assertRaises(ValueError):
            s.keep(c, {"symptom": "x", "turns": "everything"})

    def test_delete_removes_everything(self):
        s = store.MemoryStore(); c = s.open()
        s.keep(c, {"symptom": "x", "canon": "none"}); s.delete(c)
        self.assertNotIn(c, s.turns); self.assertNotIn(c, s.kept)


if __name__ == "__main__":
    unittest.main()
