"""The product play-books' form: every play-book has its sections, and every row of its Judgements table cites a
decision record (rules/product-development.md §3, d-work #9). That each citation names a record, and that each record
homed in a play-book is cited there, is the core dmc guard's (dyad/guards/agent/dmc.py)."""
import json, re, unittest
from pathlib import Path

CRAFT = Path(__file__).resolve().parents[1]
BOOKS = sorted((CRAFT / "playbooks").glob("*.md"))
SECTIONS = ("## Trigger", "## Steps", "## Judgements", "## Questions", "## Evidence")
CITE = re.compile(r"`dmc:([a-z0-9][a-z0-9-]*)`")


def judgements(text: str) -> list[str]:
    """The table rows of the Judgements section, header and separator dropped."""
    body = text.split("## Judgements", 1)[1].split("\n## ", 1)[0]
    rows = [l for l in body.splitlines() if l.startswith("|")]
    return rows[2:]


class PlaybookTests(unittest.TestCase):
    def test_the_lifecycle_has_its_play_books(self):
        names = {p.stem for p in BOOKS}
        self.assertTrue({"product-development", "build", "test", "provider", "deploy",
                         "operate", "evolve"} <= names, names)

    def test_every_play_book_has_its_sections(self):
        for p in BOOKS:
            with self.subTest(p.name):
                text = p.read_text()
                for s in SECTIONS:
                    self.assertIn(s, text)

    def test_every_judgement_cites_a_record(self):
        for p in BOOKS:
            with self.subTest(p.name):
                rows = judgements(p.read_text())
                self.assertTrue(rows, "no Judgements rows")
                for r in rows:
                    self.assertTrue(CITE.search(r), r)

    def test_every_record_homed_here_is_in_its_home_s_judgements(self):
        for f in sorted((CRAFT / "dmc").glob("*.jsonld")):
            with self.subTest(f.name):
                d = json.loads(f.read_text())
                home = CRAFT / d["dyad:home"]
                cited = {c for r in judgements(home.read_text()) for c in CITE.findall(r)}
                self.assertIn(d["identifier"], cited)


if __name__ == "__main__":
    unittest.main()
