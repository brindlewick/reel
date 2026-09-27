---
title: How the wiki is kept
type: schema
updated: 2026-09-25
---

# How the wiki is kept

This page is the contract for every other page, and for any agent working on the wiki. Read it
before adding or changing a page.

**Scope: anything the project needs to know to build reel.** What has been decided and why, how
browsers, phones and app stores really behave, and what the prototypes measured.

The shape is the LLM-wiki pattern: evidence kept unchanged in `raw/`, pages compiled from it in
`wiki/`, this page as the schema, and an append-only [log](log.md). What the project learns is
written down once and kept current, rather than worked out again each time somebody asks.

## Layers

| layer | what it is | who writes it |
|---|---|---|
| `raw/` | evidence: trials on real phones and browsers, and captured documentation. Never edited. [The contract](../raw/README.md) says what may go in. | recording a trial, capturing a source |
| `wiki/` | pages, revised freely | every operation |
| `wiki/index.md` | every page, with one line on what it holds | every operation that adds a page or changes what one says |
| `wiki/log.md` | an append-only record of every operation, newest first | every operation |

## Page kinds

**`wiki/decisions/`**: a choice about what reel is or how it is built. A decision is made, not
proven. The page states the question, the options and what each costs, and a recommendation.
Once the user answers, it records the decision, the reasons and what would reopen it. An agent
may recommend. Only the user decides.

**`wiki/concepts/`**: a claim about how something really behaves, with a standing and what would
settle it. "A mid-range phone keeps three game frames running without stutter" is one. A concept
can inform a decision. It cannot make one.

**`wiki/sources/`**: one page per captured source worth keeping: what it says, on what evidence,
and what it would mean for reel if it holds.

**`wiki/index.md`, `wiki/schema.md` and `wiki/log.md`** are the wiki's own pages.

## Front matter

Every page carries it:

```yaml
---
title: <one line>
type: decision | concept | source | schema
status: open | decided | superseded                         # decisions only
decided: YYYY-MM-DD                                          # decisions, once decided
standing: claimed | supported | mixed | refuted | settled    # concepts only
sources: [trials/<slug>, articles/<slug>]                    # raw records the page rests on
updated: YYYY-MM-DD
---
```

## The index

Every page other than the index has one line in it, in this form:

```markdown
- [Title](path.md): **status**. What the page holds, in one line.
```

A decision's line starts with its status and a concept's with its standing, so the index can be
read on its own. When a decision is made, its line changes to state the answer.

## Status of a decision

- **open**: not answered. Nothing is built on an assumed answer.
- **decided**: answered by the user on the date in `decided`. Binding until the user changes it.
- **superseded**: replaced. The page links to the decision that replaced it and says why.

A decision changes only when the user changes it. A small change is made in place and logged. A
reversal marks the page superseded and starts a new one, so the reasons for the old choice stay
readable.

## Standing of a claim

Concepts carry one of these, and the log records every change:

- **claimed**: stated, with no trial behind it yet
- **supported**: consistent with every trial that bears on it, and there are at least three
- **mixed**: trials on both sides. The page says what separates them.
- **refuted**: contradicted by trials a defender of the claim would accept
- **settled**: supported, and the trial that could have refuted it has been run

Documentation does not move a standing on its own. A vendor's page says what should happen. A
trial on a real phone says what does. A concept that cites only documentation stays claimed.

## Citations and links

- `[@trials/<slug>]` and `[@articles/<slug>]` cite a record in `raw/`. Each resolves to a path in
  this repository that anyone can open. A claim taken from evidence carries one.
- A claim with no evidence behind it says so in the sentence that makes it, with the word
  unverified, or it does not go in.
- Pages link to each other with ordinary relative links, so the links work in the repository and
  on the published site alike.

## Operations

**decide**: the user answers an open question. Write the decision, the reasons and what would
reopen it on the page. Set `status: decided` and `decided`. Rewrite the page's index line to
state the answer. Append to the log.

**record a trial**: an experiment on a real phone or browser. Put its `method.md` and its
recorded output in `raw/trials/<slug>/`. Update the standing of every concept it bears on.
Append to the log.

**ingest a source**: documentation or an article worth keeping. Capture it in
`raw/articles/<slug>/` with its `source.md`. Write its page in `wiki/sources/` and link it from
the pages it bears on. Append to the log.

**query**: a question the wiki may answer. Read the index, then the pages it points at, and
answer with citations. If the answer is worth keeping, file it as a page.

**lint**: run the check before committing any change to the wiki.

```sh
python3 scripts/wiki_lint.py
python3 -m unittest discover -s scripts
```

The script checks that:

- every page has front matter with a title, a type and a date, and a valid status or standing
- a decided decision carries the date it was decided
- a standing beyond claimed rests on at least one trial, and supported on at least three
- every citation resolves under `raw/`, and so does every source in front matter
- every relative link resolves
- every page is listed in the index with a line of its own, and a decision's or a concept's line
  starts with its current status or standing
- every trial has a `method.md`, and every capture a `source.md` giving its url and retrieval
  date

A person checks what no script can: that every claim is cited or marked unverified, that no
standing says more than its trials show, and that no decision is recorded as made that the user
did not make.

## Writing

Plain, short sentences. A person playing games in reel is a player. The user is the person
directing the work. Name no people, hosts or paths outside this repository.

## Publishing

`wiki/` is public. It is in this repository, and GitHub Pages publishes it on every push to
`main` that touches it (`.github/workflows/pages.yml`). `raw/` is not published as pages. A
citation is a path in the repository.
