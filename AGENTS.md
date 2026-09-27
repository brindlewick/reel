# reel

**This file is the canonical context for every agent working in this repository, whatever
harness it runs under.** `CLAUDE.md` is a link to it.

## What it is

A feed of playable games. The screen shows one game at a time, and a swipe moves to a different
game, the way a swipe moves to the next video in a short-video app.

## Where it stands

There is no code yet. The decisions [the first version](wiki/decisions/first-version.md) depends
on are made, and the code starts from them. A few questions are still open in the wiki.

## Read the wiki index first

[`wiki/index.md`](wiki/index.md) lists every page in the wiki, with one line on what each holds.
Read it at the start of any task, then the pages the task touches. It is kept short so that
reading it costs little. [`wiki/schema.md`](wiki/schema.md) is the contract for how pages are
written and kept. Read it before changing the wiki.

The wiki records what the project has decided and what it knows. This file says how to work
here. Do not restate one in the other.

## Decisions are not an agent's to make

Every decision page has a status.

- **open**: not answered yet. Do not answer it yourself, and do not build anything that assumes
  an answer. Ask the user, and give them the options the page lists.
- **decided**: binding. Build to it. If the work shows it is wrong, say so and ask. Do not work
  around it.
- **superseded**: replaced by the decision the page links to.

A question becomes decided when the user answers it. Record the answer on the page, in its index
line and in the log, in the same change.

## Working on this repository

- Work in a git worktree under `.worktrees/`, one branch per change, and open a pull request.
  The user merges.
- A new page goes in the index in the same change, with its one line. Every change to the wiki
  adds an entry to [the log](wiki/log.md).
- Run the wiki check before committing a change to the wiki. It fails on a page missing from
  the index, an index line whose status is out of date, a broken link, and the other faults
  [the schema](wiki/schema.md) lists. It also runs on every pull request.

  ```sh
  python3 scripts/wiki_lint.py                 # faults on stdout, exit 1 if any
  python3 -m unittest discover -s scripts      # the check's own tests
  ```

- Commit messages and pull requests: short, factual, present tense.

## Vocabulary

**feed**: the vertical sequence of games, one on screen at a time · **game**: one playable entry
in the feed · **player**: a person playing games in reel. The wiki never calls a player a user,
so that **the user** always means the person directing the work.
