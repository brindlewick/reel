---
title: Swipe and game input
type: decision
status: open
updated: 2026-09-27
---

# Swipe and game input

**Question.** How does the feed tell a swipe to another game apart from the game's own touch
input?

**Status: open.**

## Why it matters

Many games use vertical swipes. If the feed takes every vertical swipe, those games cannot be
played. If the game takes every touch, the player cannot leave it. This shapes how reel feels
more than any other choice in the first version.

There is a technical side as well. In the apps, the feed and the game's web view receive the
same touches, and the app has to decide which one a swipe belongs to. How it decides depends on
[the app shell](app-shell.md). On the web, a touch on a game lands inside the game's frame,
where the feed's page does not see it, and a phone browser has gestures of its own. How reliably
either can tell a swipe apart while a game handles touches of its own is unverified. Where it
cannot, the game reports the swipe to the feed through the [contract](game-format.md). Without a
touch screen, the swipe becomes the scroll wheel, a trackpad or the arrow keys, as
[the web version](web-version.md) decides.

## Options

**Swipe anywhere, and games do not use vertical swipes.** Closest to a video feed, and the
simplest to learn. It rules out games built on vertical swipes or drags.

**Swipe from an edge strip.** A strip at one edge of the screen belongs to the feed, and the rest
belongs to the game. Any game fits, and the feed sees the swipe because the strip is its own.
The costs: it is less natural, it needs a visible cue, and phones keep some edges for their own
gestures (unverified: which edges, on which phones).

**A button for the next game.** No conflict at all, but it drops the swipe the idea is built on.

**Each game declares what it uses.** Games that leave vertical swipes alone get swipe anywhere,
and games that use them get the edge strip. The costs: two behaviours for players to learn, and
it relies on each game declaring correctly.

## Recommendation

Swipe anywhere for the first version, with in-house games that leave vertical swipes alone. The
first version then tests whether the apps and the web tell the swipe apart reliably, and falls
back to the game reporting it through the contract where they do not. Revisit this before any game by another
author arrives, since that is when the edge strip or a declaration would be needed.

## What depends on it

[Game format](game-format.md), [game lifecycle](game-lifecycle.md) and
[the first version](first-version.md).
