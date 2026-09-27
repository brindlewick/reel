---
title: The first version
type: decision
status: open
updated: 2026-09-27
---

# The first version

**Question.** What is the smallest build that shows whether swiping to a new game works, and how
will we know?

**Status: open.** This page holds a proposal. It follows from the other decisions, and changes if
they do.

## Proposal

- reel on Android, iOS and the web, built as [the app shell](app-shell.md) decides, with no
  accounts and no data collection. The apps carry the games inside them, and the web version and
  its games are static files, so there is no server.
- A vertical feed that shows one game at a time and snaps to each.
- Four or five small games written for it, following the [game format](game-format.md). For
  example: a one-button flying game, a reaction timer, a block-stacking game and a
  tap-the-target game. None uses vertical swipes.
- A manifest in one file that lists them, in a [fixed order](feed-order.md).
- The live window and pausing from the [game lifecycle](game-lifecycle.md).
- The games in TypeScript. The app's language follows from [the app shell](app-shell.md).

## How we will know it works

On a mid-range Android phone and a mid-range iPhone:

1. The next game is playable within a second of a swipe.
2. A swipe is never taken as game input, and game input never moves the feed.
3. A game the player swipes back to behaves as [coming back to a game](game-return.md) decides.
4. Three games stay live without the feed or the active game stuttering.

And across the platforms:

5. The same game bundles run unchanged on Android, iOS and the web.

Each of these becomes a trial, recorded in `raw/trials/` with its method, so the result can be
checked and repeated.

## Still to settle

- Which phones the trials run on, and which of them counts as mid-range.

## Depends on

[Platform](platform.md), [which phones first](mobile-os.md), [the app shell](app-shell.md),
[the web version](web-version.md), [where games come from](game-sources.md),
[game format](game-format.md), [swipe and game input](swipe-gesture.md),
[starting a game](game-start.md), [coming back to a game](game-return.md),
[game lifecycle](game-lifecycle.md) and [game length](game-length.md).
