"""The adversarial set (playbooks/test.md; dmc:test-level adversarial, dmc:fixture-source, dmc:test-failure).

The seeds are the operator's own symptom prompts, named by provenance entry in tests/fixtures/adversarial/seeds.json
and read at the pin from a local dyad-system checkout (`git config prompt-therapy.canon <path>`, per checkout, never
tracked); the variants (reworded, combined, hostile, off-topic) are written for the test. Every member is walked
against the canon at the same pin with the fake provider, and fails when the walk:
- diagnoses: an outgoing line matches the diagnosis pattern, or a cause is offered as anything but a question;
- names a person: a name the member wrote is said back or kept;
- keeps without consent: anything is kept without an exact yes at the consent step;
- misses its path: none of its canon entries is offered (an off-topic member: any entry is offered), the walk does not
  reach consent and close, or a breach had to be caught.
Without a checkout the set skips with one line; the synthetic harness (tests/test_walk.py) still runs.
"""
import json, subprocess, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import canon, provider, seeds, store, walk

HERE = Path(__file__).resolve().parent / "fixtures" / "adversarial"
PIN = json.loads((HERE / "pin.json").read_text())
SEEDS = json.loads((HERE / "seeds.json").read_text())
VARIANTS = json.loads((HERE / "variants.json").read_text())
KINDS = ("reworded", "combined", "hostile", "off-topic")


def checkout() -> Path | None:
    r = subprocess.run(["git", "config", "--get", "prompt-therapy.canon"], capture_output=True, text=True,
                       cwd=Path(__file__).resolve().parent)
    p = Path(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip() else None
    return p if p and p.is_dir() else None


REPO = checkout()


def drive(c, text: str, consent: str, want: list[str]):
    """Walk one member to its end, choosing at each step as a user who means `want` would."""
    s = store.MemoryStore()
    w = walk.Walk(c, provider.FakeProvider(), s)
    said = [w.start(), w.receive(text), w.receive("yes")]
    offered = [e.id for e in w.offered] if w.state == "match" else []
    pick = next((i for i, e in enumerate(offered, 1) if e in want), len(offered) + 1)
    said.append(w.receive(str(pick)))
    for _ in range(12):
        if w.state == "walk":
            said.append(w.receive("1"))
        elif w.state == "anchor":
            said.append(w.receive("yes"))
        else:
            break
    reached_consent = w.state == "consent"
    said.append(w.receive(consent))
    return w, s, said, offered, reached_consent


@unittest.skipIf(REPO is None, "adversarial set: no dyad-system checkout (git config prompt-therapy.canon <path>); skipped")
class AdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        problems = seeds.verify(REPO, PIN)
        if problems:
            raise AssertionError("the pin does not hold: " + "; ".join(problems))
        cls.canon = canon.load_at(REPO, PIN["commit"])
        cls.words = seeds.resolve(REPO, PIN, SEEDS)

    def members(self):
        for sd in SEEDS:
            for consent in ("yes", "no"):
                yield f"{sd['id']}/seed/{consent}", self.words[sd["id"]], consent, [], sd["canon"]
        for v in VARIANTS:
            yield v["id"], v["text"], v["consent"], v["names"], v["canon"]

    def test_the_set_is_whole(self):
        self.assertEqual(len(self.words), len(SEEDS))
        for sd in SEEDS:
            kinds = sorted(v["kind"] for v in VARIANTS if v["seed"] == sd["id"])
            self.assertEqual(kinds, sorted(KINDS), sd["id"])
            self.assertTrue(set(sd["canon"]) <= set(self.canon.entries), sd["id"])

    def test_every_member_holds_the_never_rules_and_its_path(self):
        for name, text, consent, names, want in self.members():
            with self.subTest(name):
                w, s, said, offered, reached = drive(self.canon, text, consent, want)
                self.assertEqual(w.breaches, 0, "a breach had to be caught")
                self.assertTrue(said[0].startswith(provider.NOT_THERAPY))
                for line in said:
                    self.assertIsNone(walk.DIAGNOSIS.search(line), line)
                    for n in names:
                        self.assertNotIn(n, line)
                    for l in line.splitlines():
                        if "Could it be" in l:
                            self.assertTrue(l.rstrip().endswith("?"), l)
                kept = s.kept.get(w.cid)
                self.assertEqual(kept is not None, consent in walk.YES, f"consent {consent!r}")
                if kept:
                    self.assertEqual(set(kept), set(store.KEPT_FIELDS))
                    for n in names:
                        self.assertNotIn(n, json.dumps(kept))
                if want:
                    self.assertTrue(set(offered) & set(want), f"offered {offered}, wanted one of {want}")
                else:
                    self.assertEqual(offered, [], "an off-topic member was offered a canon entry")
                self.assertTrue(reached, "the walk did not reach consent")
                self.assertEqual(w.state, "close")
                self.assertNotIn(w.cid, s.turns)


class PinShapeTests(unittest.TestCase):
    def test_the_pin_names_a_full_commit_and_the_records_the_seeds_read(self):
        self.assertRegex(PIN["commit"], r"^[0-9a-f]{40}$")
        for sd in SEEDS:
            self.assertIn(seeds.record_path(sd["record"]), PIN["files"])
        self.assertIn(f"{canon.CANVAS}/symptoms.md", PIN["files"])

    def test_no_fixture_copies_a_seeds_words(self):
        self.assertTrue(all(set(sd) == set(seeds.SEED_KEYS) for sd in SEEDS))


if __name__ == "__main__":
    unittest.main()
