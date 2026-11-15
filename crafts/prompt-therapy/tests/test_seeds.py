"""seeds.py: a seed holds no words; its words are read at the pin, and a pin that does not hash fails (d-work #2)."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import canon, seeds

RECORD = "# Provenance #7\n\n## 1 prompt 2026-01-01\n\n```\nfirst words\n```\n\n## 2 prompt 2026-01-02\n\n```\nlist:\n\n* one thing\n* another thing\n```\n"


class EntryTests(unittest.TestCase):
    def test_entry_text_and_bullets(self):
        self.assertEqual(seeds.entry_text(RECORD, 1), "first words")
        self.assertEqual(seeds.bullets(seeds.entry_text(RECORD, 2)), ["one thing", "another thing"])
        self.assertEqual(seeds.words_of(RECORD, {"id": "s", "entry": 2, "bullet": 2}), "another thing")
        with self.assertRaises(ValueError):
            seeds.entry_text(RECORD, 3)
        with self.assertRaises(ValueError):
            seeds.words_of(RECORD, {"id": "s", "entry": 1, "bullet": 1})


class PinTests(unittest.TestCase):
    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        run = lambda *a: subprocess.run(["git", *a], cwd=self.repo, check=True, capture_output=True, env=canon.dyadlib.git_env())
        p = self.repo / seeds.record_path(7); p.parent.mkdir(parents=True); p.write_text(RECORD)
        run("init", "-q"); run("add", "."); run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "c")
        self.commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.repo, capture_output=True, text=True).stdout.strip()
        self.pin = {"commit": self.commit, "files": {seeds.record_path(7): seeds.sha256(RECORD)}}

    def test_a_holding_pin_resolves_its_seeds(self):
        self.assertEqual(seeds.verify(self.repo, self.pin), [])
        got = seeds.resolve(self.repo, self.pin, [{"id": "a", "record": 7, "entry": 2, "bullet": 1, "canon": []}])
        self.assertEqual(got, {"a": "one thing"})

    def test_a_pin_that_does_not_hash_fails(self):
        bad = {"commit": self.commit, "files": {seeds.record_path(7): "0" * 64}}
        self.assertTrue(seeds.verify(self.repo, bad))

    def test_an_unpinned_record_is_refused(self):
        with self.assertRaises(ValueError):
            seeds.resolve(self.repo, {"commit": self.commit, "files": {}}, [{"id": "a", "record": 7, "entry": 1, "bullet": None, "canon": []}])


if __name__ == "__main__":
    unittest.main()
