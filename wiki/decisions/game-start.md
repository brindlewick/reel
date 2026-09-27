---
title: Starting a game
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Starting a game

**Question.** When a game comes on screen, does it start at once or wait for the player? And
when does sound start?

**Status: decided on 2026-09-27.**

## Options

**Starts at once, like a video that plays on its own.** The shortest path from a swipe to play.
The costs: the player may not be ready, and the first seconds of a timed game are lost.

**Waits on its own start screen, and starts on the first touch.** The game is live and visible at
once, and play begins when the player touches it, as many arcade games already do. No time is
lost, and the feed adds no screen of its own.

**A cover from the feed, with a play button.** Every game looks the same before it starts. The
costs: an extra tap for every game, which adds up over a feed and feels closer to a menu.

## Sound

On the web, a browser plays no sound until the player has touched or clicked the page. The apps
can let their web views play sound without a touch (unverified: from memory, not yet tried). So
in the apps, when sound starts is a choice, not a limit.

## Decision

The game waits on its own start screen and starts on the first touch. Sound starts when play
starts, so the feed never makes a sound the player did not ask for, and the rule is the same on
all three platforms.

## What would reopen it

Players finding the start screen an extra step, for example if the first version's trials show
the time from a swipe to play feels long.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
