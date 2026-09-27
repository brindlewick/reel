"""Tests for wiki_lint.

Well-formed fixtures must pass, and each check must fail on its own fault, asserted on its own
message, so that a fixture cannot pass a test by failing for some other reason.
"""
from __future__ import annotations

import unittest

from wiki_lint import lint

SOURCE_MD = "---\nurl: https://example.org/page\nretrieved: 2026-01-01\n---\n"


def page(kind: str, body: str = "Body.\n", **fields: str) -> str:
    lines = {"title": "A page", "type": kind, **fields, "updated": "2026-01-01"}
    return "---\n" + "".join(f"{k}: {v}\n" for k, v in lines.items()) + "---\n\n" + body


def clean() -> dict[str, str]:
    return {
        "wiki/index.md": page(
            "schema",
            "- [A choice](decisions/choice.md): **open**. Which way to go.\n"
            "- [A claim](concepts/claim.md): **claimed**. How something behaves.\n"
            "- [Log](log.md): every change.\n",
        ),
        "wiki/log.md": page("schema"),
        "wiki/decisions/choice.md": page("decision", status="open"),
        "wiki/concepts/claim.md": page("concept", standing="claimed"),
        "raw/README.md": "",
    }


def with_index_line(files: dict[str, str], old: str, new: str) -> dict[str, str]:
    files["wiki/index.md"] = files["wiki/index.md"].replace(old, new)
    return files


class Lint(unittest.TestCase):
    def assert_fault(self, files: dict[str, str], message: str) -> None:
        faults = lint(files)
        self.assertTrue(any(message in f for f in faults), f"no fault containing {message!r} in {faults}")

    # Negative controls: well-formed wikis pass.

    def test_a_clean_wiki_passes(self) -> None:
        self.assertEqual(lint(clean()), [])

    def test_a_decided_decision_and_a_settled_concept_with_their_evidence_pass(self) -> None:
        files = clean()
        files["wiki/decisions/choice.md"] = page("decision", status="decided", decided="2026-01-02")
        files["wiki/concepts/claim.md"] = page(
            "concept", "Seen in [@trials/t1].\n", standing="settled", sources="[trials/t1, articles/a1]"
        )
        files["raw/trials/t1/method.md"] = "Method.\n"
        files["raw/articles/a1/source.md"] = SOURCE_MD
        with_index_line(files, "**open**", "**decided**")
        with_index_line(files, "**claimed**", "**settled**")
        self.assertEqual(lint(files), [])

    def test_notation_in_code_is_not_checked(self) -> None:
        files = clean()
        files["wiki/log.md"] = page("schema", "Cite `[@trials/<slug>]`, link `[x](nowhere.md)`.\n```\n[y](gone.md)\n```\n")
        self.assertEqual(lint(files), [])

    # Positive controls: one per check.

    def test_a_page_without_front_matter(self) -> None:
        files = clean()
        files["wiki/log.md"] = "# Log\n"
        self.assert_fault(files, "wiki/log.md: no front matter")

    def test_front_matter_without_a_title(self) -> None:
        files = clean()
        files["wiki/log.md"] = "---\ntype: schema\nupdated: 2026-01-01\n---\n"
        self.assert_fault(files, "wiki/log.md: front matter has no title")

    def test_an_unknown_type(self) -> None:
        files = clean()
        files["wiki/log.md"] = page("notes")
        self.assert_fault(files, "type 'notes' is not one of")

    def test_a_decision_without_a_status(self) -> None:
        files = clean()
        files["wiki/decisions/choice.md"] = page("decision")
        self.assert_fault(files, "decision with no status")

    def test_an_unknown_status(self) -> None:
        files = clean()
        files["wiki/decisions/choice.md"] = page("decision", status="pending")
        self.assert_fault(files, "status 'pending' is not one of")

    def test_a_decided_decision_without_a_date(self) -> None:
        files = with_index_line(clean(), "**open**", "**decided**")
        files["wiki/decisions/choice.md"] = page("decision", status="decided")
        self.assert_fault(files, "decided decision has no decided date")

    def test_a_concept_without_a_standing(self) -> None:
        files = clean()
        files["wiki/concepts/claim.md"] = page("concept")
        self.assert_fault(files, "concept with no standing")

    def test_an_unknown_standing(self) -> None:
        files = clean()
        files["wiki/concepts/claim.md"] = page("concept", standing="probable")
        self.assert_fault(files, "standing 'probable' is not one of")

    def test_a_standing_moved_by_documentation_alone(self) -> None:
        files = with_index_line(clean(), "**claimed**", "**settled**")
        files["raw/articles/a1/source.md"] = SOURCE_MD
        files["wiki/concepts/claim.md"] = page("concept", standing="settled", sources="[articles/a1]")
        self.assert_fault(files, "rests on no trial")

    def test_supported_on_fewer_than_three_trials(self) -> None:
        files = with_index_line(clean(), "**claimed**", "**supported**")
        files["raw/trials/t1/method.md"] = "Method.\n"
        files["wiki/concepts/claim.md"] = page("concept", standing="supported", sources="[trials/t1]")
        self.assert_fault(files, "three are needed")

    def test_a_source_in_front_matter_that_does_not_resolve(self) -> None:
        files = clean()
        files["wiki/concepts/claim.md"] = page("concept", standing="claimed", sources="[trials/missing]")
        self.assert_fault(files, "source trials/missing does not resolve under raw/")

    def test_a_citation_that_does_not_resolve(self) -> None:
        files = clean()
        files["wiki/concepts/claim.md"] = page("concept", "See [@trials/missing].\n", standing="claimed")
        self.assert_fault(files, "citation [@trials/missing] does not resolve under raw/")

    def test_a_link_that_does_not_resolve(self) -> None:
        files = clean()
        files["wiki/log.md"] = page("schema", "See [the page](nowhere.md).\n")
        self.assert_fault(files, "wiki/log.md: link to nowhere.md does not resolve")

    def test_no_index(self) -> None:
        files = clean()
        del files["wiki/index.md"]
        self.assert_fault(files, "wiki/index.md: missing")

    def test_a_page_missing_from_the_index(self) -> None:
        files = clean()
        files["wiki/decisions/another.md"] = page("decision", status="open")
        self.assert_fault(files, "wiki/decisions/another.md: not listed in wiki/index.md")

    def test_an_index_entry_without_a_line(self) -> None:
        files = with_index_line(clean(), "- [Log](log.md): every change.", "- [Log](log.md)")
        self.assert_fault(files, "wiki/log.md: listed in wiki/index.md with no line")

    def test_an_index_line_with_a_stale_status(self) -> None:
        files = clean()
        files["wiki/decisions/choice.md"] = page("decision", status="decided", decided="2026-01-02")
        self.assert_fault(files, "does not start with **decided**, its status")

    def test_an_index_line_with_a_stale_standing(self) -> None:
        files = clean()
        files["raw/trials/t1/method.md"] = "Method.\n"
        files["wiki/concepts/claim.md"] = page("concept", standing="refuted", sources="[trials/t1]")
        self.assert_fault(files, "does not start with **refuted**, its standing")

    def test_a_trial_without_a_method(self) -> None:
        files = clean()
        files["raw/trials/t1/timings.csv"] = ""
        self.assert_fault(files, "raw/trials/t1: trial has no method.md")

    def test_a_capture_without_a_source_file(self) -> None:
        files = clean()
        files["raw/articles/a1/page.html"] = ""
        self.assert_fault(files, "raw/articles/a1: capture has no source.md")

    def test_a_source_file_without_a_url(self) -> None:
        files = clean()
        files["raw/articles/a1/source.md"] = "---\nretrieved: 2026-01-01\n---\n"
        self.assert_fault(files, "source.md has no url")

    def test_a_source_file_without_a_retrieval_date(self) -> None:
        files = clean()
        files["raw/articles/a1/source.md"] = "---\nurl: https://example.org/page\n---\n"
        self.assert_fault(files, "source.md has no retrieved")


if __name__ == "__main__":
    unittest.main()
