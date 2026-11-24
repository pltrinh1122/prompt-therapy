"""thread.py: reading the labels in a reply, numbering the next questions, and checking an email before it is sent
(playbooks/user-research.md, steps 11, 13 and 16). Every reply and email here is made up for the test
(dmc:fixture-source, synthetic); none comes from a real thread."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import thread

SIG = "Wren (AI), writing on behalf of [operator name]"


WHY_WHERE = "**This round:** times a long session lost track.\n**Where we are:** about three short rounds left, or stop anytime."


def email(body: str, why_where: str = WHY_WHERE) -> str:
    return f"{why_where}\n\n{body}\n\nReply under any number you like, for example `Q4: …`. Skip any you want.\n\n{SIG}"


class ParseTests(unittest.TestCase):
    def test_labels_on_their_own_lines(self):
        parts, rest = thread.parse("Q1: it said tests passed.\nQ3: lost an afternoon.")
        self.assertEqual(parts, [("Q1", "it said tests passed."), ("Q3", "lost an afternoon.")])
        self.assertEqual(rest, "")

    def test_labels_after_a_sentence_on_one_line(self):
        parts, _ = thread.parse("N1 yes. Q4: it rushed. Q6: now I ask for the output.")
        self.assertEqual([l for l, _ in parts], ["N1", "Q4", "Q6"])
        self.assertEqual(parts[0], ("N1", "yes."))

    def test_profile_label(self):
        parts, _ = thread.parse("P yes")
        self.assertEqual(parts, [("P", "yes")])

    def test_unlabelled_text_is_left_for_judgement(self):
        parts, rest = thread.parse("Thanks for the note.\nQ2: mostly reports.")
        self.assertEqual(rest, "Thanks for the note.")
        self.assertEqual(parts, [("Q2", "mostly reports.")])

    def test_quoted_earlier_mail_is_dropped(self):
        reply = "Q1: spreadsheets.\n\nOn Mon, Wren wrote:\n> **Q1.** Which AI tools do you use?\n> Q2: x"
        parts, rest = thread.parse(reply)
        self.assertEqual(parts, [("Q1", "spreadsheets.")])
        self.assertEqual(rest, "")

    def test_a_number_inside_a_sentence_is_not_a_label(self):
        parts, rest = thread.parse("as I said in Q4 it guessed")
        self.assertEqual(parts, [])
        self.assertEqual(rest, "as I said in Q4 it guessed")


class NextTests(unittest.TestCase):
    def test_numbers_follow_the_highest(self):
        self.assertEqual(thread.next_numbers([1, 2, 3, 7]), [8, 9])

    def test_first_numbers(self):
        self.assertEqual(thread.next_numbers([], 3), [1, 2, 3])


class WatchGapTests(unittest.TestCase):
    def test_gaps_double_from_two(self):
        self.assertEqual([thread.watch_gap(n) for n in range(1, 7)], [2, 4, 8, 16, 32, 64])

    def test_held_at_the_cap(self):
        self.assertEqual(thread.watch_gap(7), 64)
        self.assertEqual(thread.watch_gap(50), 64)

    def test_at_most_24_checks_a_day_at_the_cap(self):
        self.assertEqual(24 * 60 // thread.watch_gap(30), 22)
        self.assertLessEqual(24 * 60 // thread.watch_gap(30), 24)

    def test_n_counts_from_one(self):
        with self.assertRaises(ValueError):
            thread.watch_gap(0)


class CheckTests(unittest.TestCase):
    def test_a_good_email_passes(self):
        e = email("Thanks. Here's what I heard:\n- **Q1:** reports.\n\n**Q4 (about Q1).** Why do you think it did that?")
        self.assertEqual(thread.check(e, asked=[1, 2, 3], sent=2), [])

    def test_missing_signature(self):
        self.assertIn("signature missing", thread.check("**Q1.** What happened?", asked=[]))

    def test_too_many_new_questions(self):
        e = email("**Q1.** a?\n**Q2.** b?\n**Q3.** c?\n**Q4.** d?")
        self.assertTrue(any("too many" in p for p in thread.check(e, asked=[])))

    def test_three_new_questions_are_too_many(self):
        e = email("**Q4.** Walk me through the last time it happened.\n**Q5.** b?\n**Q6.** c?")
        self.assertTrue(any("too many" in p for p in thread.check(e, asked=[1, 2, 3])))

    def test_one_story_and_one_test_pass(self):
        e = email("**Q4.** Walk me through the last time it happened.\n\n"
                  "**Q5.** Other people have seen this get worse late in a session. "
                  "Does that match what you've seen, or not?")
        self.assertEqual(thread.check(e, asked=[1, 2, 3]), [])

    def test_why_line_required(self):
        e = email("Thanks.", why_where="**Where we are:** about two rounds left.")
        self.assertIn("the why line missing: a line opening **This round:**", thread.check(e, asked=[]))

    def test_where_line_required(self):
        e = email("Thanks.", why_where="**This round:** what planning looks like.")
        self.assertIn("the where line missing: a line opening **Where we are:**", thread.check(e, asked=[]))

    def test_an_empty_why_line_fails(self):
        e = email("Thanks.", why_where="**This round:**\n**Where we are:** about two rounds left.")
        self.assertTrue(any("why line missing" in p for p in thread.check(e, asked=[])))

    def test_new_questions_numbered_next(self):
        e = email("**Q6.** What happened?")
        self.assertTrue(any("next in turn" in p for p in thread.check(e, asked=[1, 2, 3])))

    def test_research_words_fail(self):
        e = email("**Q4.** What was the root cause?")
        self.assertTrue(any("research words" in p for p in thread.check(e, asked=[1, 2, 3])))

    def test_because_is_not_a_research_word(self):
        e = email("**Q4.** What did you do because of it?")
        self.assertEqual(thread.check(e, asked=[1, 2, 3]), [])

    def test_skipped_question_asked_again(self):
        e = email("**Q2.** What kind of work do you hand to it?")
        self.assertTrue(any("asked again" in p for p in thread.check(e, asked=[1, 2, 3], skipped=[2])))

    def test_q1_may_be_asked_once_more(self):
        e = email("**Q1.** Which AI tool was that?")
        self.assertEqual(thread.check(e, asked=[1, 2, 3], skipped=[1], reask_q1=True), [])

    def test_wren_is_never_claude(self):
        e = email("I'm Wren, an AI assistant built on Claude.")
        self.assertIn("names Claude as what Wren is", thread.check(e, asked=[]))

    def test_no_product_before_q1_is_answered(self):
        e = email("**Q4.** When Claude did that, what happened next?")
        self.assertTrue(any("product" in p for p in thread.check(e, asked=[1, 2, 3], q1_answered=False)))

    def test_a_product_in_their_own_words_passes(self):
        e = email("**Q4.** When Claude did that, what happened next?")
        self.assertEqual(thread.check(e, asked=[1, 2, 3], q1_answered=False, said=["claude"]), [])

    def test_profile_block_holds_only_its_fields(self):
        good = email("**P.** Works in accounting, senior role, 6–10 years, uses AI tools daily.")
        bad = email("**P.** Works at a firm downtown, 41 years old.")
        self.assertEqual(thread.check(good, asked=[1, 2, 3, 4]), [])
        self.assertIn("profile block holds more than its fields", thread.check(bad, asked=[1, 2, 3, 4]))

    def test_too_long(self):
        e = email("word " * 210)
        self.assertTrue(any("too long" in p for p in thread.check(e, asked=[])))

    def test_ceiling(self):
        e = email("Thanks.")
        self.assertTrue(any("ceiling" in p for p in thread.check(e, asked=[], sent=20, ceiling=20)))


if __name__ == "__main__":
    unittest.main()
