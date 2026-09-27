---
title: Feed order
type: decision
status: open
updated: 2026-09-25
---

# Feed order

**Question.** What decides which game comes next?

**Status: open.**

## Options

**A fixed order, chosen by hand.** The same for every player, with no data and no server. The
costs: it does not learn, and a returning player sees the same sequence.

**A shuffle of a hand-picked set.** Each visit differs, still with no server.

**Recommendations for each player**, from what they played and for how long, the way a video
feed ranks what comes next. The costs: a way to recognise a returning player, collecting what
they do, a position on privacy, a ranking system, and enough games for ranking to matter.

## Recommendation

A fixed order for the first version, since a trial is easier to compare when every run sees the
same games in the same order. Then a shuffle once there are enough games.

Whether recommendations are part of the core idea is worth deciding now. If they are, the first
version could keep the signals a ranking would use, such as the time spent on each game and
quick skips, on the phone only.

## What depends on it

Nothing in the first version.
