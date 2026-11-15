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
