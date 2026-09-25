---
title: The first version
type: decision
status: open
updated: 2026-09-25
---

# The first version

**Question.** What is the smallest build that shows whether swiping to a new game works, and how
will we know?

**Status: open.** This page holds a proposal. It follows from the other decisions, and changes if
they do.

## Proposal

- A single web page, with no server of its own, no accounts and no data collection.
- A vertical feed that shows one game at a time and snaps to each.
- Four or five small games written for it, following the [game format](game-format.md). For
  example: a one-button flying game, a reaction timer, a block-stacking game and a
  tap-the-target game. None uses vertical swipes.
- A manifest in one file that lists them, in a [fixed order](feed-order.md).
- The live window and pausing from the [game lifecycle](game-lifecycle.md).
- TypeScript. The build tool is chosen when the code starts.

## How we will know it works

On a mid-range phone:

1. The next game is playable within a second of a swipe.
2. A swipe is never taken as game input, and game input never moves the feed.
3. A game the player swipes back to behaves as [coming back to a game](game-return.md) decides.
4. Three games stay live without the feed or the active game stuttering.

Each of these becomes a trial, recorded in `raw/trials/` with its method, so the result can be
checked and repeated.

## Still to settle

- Which phones and browsers the trials run on, and which of them counts as mid-range.

## Depends on

[Platform](platform.md), [where games come from](game-sources.md),
[game format](game-format.md), [swipe and game input](swipe-gesture.md),
[starting a game](game-start.md), [coming back to a game](game-return.md),
[game lifecycle](game-lifecycle.md) and [game length](game-length.md).
