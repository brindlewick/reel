---
title: Starting a game
type: decision
status: open
updated: 2026-09-25
---

# Starting a game

**Question.** When a game comes on screen, does it start at once or wait for the player? And
when does sound start?

**Status: open.**

## Options

**Starts at once, like a video that plays on its own.** The shortest path from a swipe to play.
The costs: the player may not be ready, and the first seconds of a timed game are lost.

**Waits on its own start screen, and starts on the first touch.** The game is live and visible at
once, and play begins when the player touches it, as many arcade games already do. No time is
lost, and the feed adds no screen of its own.

**A cover from the feed, with a play button.** Every game looks the same before it starts. The
costs: an extra tap for every game, which adds up over a feed and feels closer to a menu.

## Sound

Browsers block sound until the player has touched the page (unverified: the exact rules differ
by browser and have not been captured). Whatever the choice above, the feed can start muted and
turn sound on for every game after the first touch.

## Recommendation

The game waits on its own start screen and starts on the first touch. The first touch in a
session also turns sound on.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
