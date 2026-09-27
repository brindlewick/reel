---
title: Coming back to a game
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Coming back to a game

**Question.** When a player swipes back to a game they left, does it resume where they left it,
or start fresh?

**Status: decided on 2026-09-27.**

## Options

**Always resume.** Like going back to a paused video. The costs: every game must stay loaded, or
save and restore its state, and every game must support pause. Phone memory limits how many
games can stay loaded (unverified: how many a mid-range phone can hold).

**Always start fresh.** Nothing is kept, and a game is unloaded as soon as it leaves the screen.
The cost: an accidental swipe loses the player's progress.

**Resume only the game just left.** The previous game stays loaded and paused, which the
[game lifecycle](game-lifecycle.md) proposes anyway, and anything further back starts fresh. It
covers the accidental swipe, the case that matters most, at no extra memory cost.

## Decision

Resume only the game just left. Anything further back starts fresh.

## What would reopen it

Players losing progress they wanted to keep in games further back, or the live window turning
out too costly on a mid-range phone.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
