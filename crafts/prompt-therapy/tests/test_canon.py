"""canon.py: the canon and why-tree formats read into one graph (fixtures under tests/fixtures/canon)."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import canon

CANVAS = Path(__file__).resolve().parent / "fixtures" / "canon"


class CanonTests(unittest.TestCase):
    def setUp(self):
        self.c = canon.load(CANVAS)

    def test_entries_stop_at_candidates(self):
        self.assertEqual(sorted(self.c.entries), ["S1", "S2", "S3"])

    def test_an_entry_is_rooted_by_its_tree_sources_only(self):
        self.assertEqual(self.c.entries["S1"].roots, [("demo", "D0")])
        self.assertEqual(self.c.entries["S3"].roots, [])

    def test_children_and_links_are_both_options(self):
        self.assertEqual([n.id for n in self.c.options("demo", "D0")], ["D0.1", "D0.2"])
        self.assertEqual([n.id for n in self.c.options("demo", "D0.2")], ["D0.1.1"])
        self.assertEqual(self.c.trees["demo"]["D0.1.1"].kind, "anchor")

    def test_summary_cli(self):
        self.assertEqual(canon.main(["summary", str(CANVAS)]), 0)
        self.assertEqual(canon.main([]), 2)


if __name__ == "__main__":
    unittest.main()


class PinnedReaderTests(unittest.TestCase):
    """load_at: the same canon read at a commit of a checkout, a reference tree included (d-work #2)."""
    def setUp(self):
        import subprocess, tempfile
        self.repo = Path(tempfile.mkdtemp())
        run = lambda *a: subprocess.run(["git", *a], cwd=self.repo, check=True, capture_output=True, env=canon.dyadlib.git_env())
        cv = self.repo / "site" / "lean-canvas"
        (cv / "seg").mkdir(parents=True); (cv / "reference").mkdir()
        (cv / "symptoms.md").write_text("## S1 It states something false.\nsources: observed:1#1, ref:X0\n## candidates\n")
        (cv / "seg" / "why-tree.md").write_text("A0 [symptom; H] a\n  A0.1 [anchor; H] b\n")
        (cv / "reference" / "ref.md").write_text("X0 [symptom; H] false\n  X0.1 [anchor; H] care\n")
        (cv / "why-tree.md").write_text("M0 [seg: symptom; H] merged, not read\n")
        run("init", "-q"); run("add", "."); run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "c")
        self.commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.repo, capture_output=True, text=True).stdout.strip()

    def test_load_at_reads_segments_and_reference_trees(self):
        c = canon.load_at(self.repo, self.commit)
        self.assertEqual(sorted(c.trees), ["ref", "seg"])
        self.assertEqual(c.entries["S1"].roots, [("ref", "X0")])
        self.assertEqual([n.id for n in c.options("ref", "X0")], ["X0.1"])

    def test_load_and_load_at_agree(self):
        a = canon.load(self.repo / "site" / "lean-canvas")
        b = canon.load_at(self.repo, self.commit)
        self.assertEqual((sorted(a.trees), sorted(a.entries)), (sorted(b.trees), sorted(b.entries)))

    def test_tree_names(self):
        self.assertEqual(canon.tree_name("seg/why-tree.md"), "seg")
        self.assertEqual(canon.tree_name("reference/ref.md"), "ref")
        self.assertIsNone(canon.tree_name("why-tree.md"))
        self.assertIsNone(canon.tree_name("seg/other.md"))
