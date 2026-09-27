---
title: Game lifecycle
type: decision
status: open
updated: 2026-09-27
---

# Game lifecycle

**Question.** How is a game loaded, run, paused and unloaded as it scrolls in and out of view?

**Status: open.** This page holds a proposal. It depends on [starting a game](game-start.md),
[coming back to a game](game-return.md), [swipe and game input](swipe-gesture.md) and
[the app shell](app-shell.md).

## Proposal

**A live window of three games**: the one on screen, the one before it and the one after it.
Anything further away is removed, and loaded again if the player comes back to it.

**One active game.** A game becomes active when most of it is on screen and the scroll has come
to rest. Only the active game gets touch input and sound. When a game stops being active, the
feed sends it `pause` and mutes it.

**A game passes through these states:**

| state | what it means |
|---|---|
| unloaded | outside the live window. Nothing is loaded. |
| loading | inside the window, and its web view is loading |
| ready | loaded, and it has sent `ready` if it follows the contract |
| active | on screen, with touch input and sound |
| paused | inside the window but off screen, and still loaded |
| failed | it did not become ready in time. The feed says so and lets the player move on. |

A game that does not follow the [contract](game-format.md) cannot be paused. It is unloaded when
it leaves the screen, so it starts fresh when the player comes back to it.

**Three is a guess.** Whether a mid-range phone keeps three web views running without stutter is
unverified, and [the first version](first-version.md) measures it.

## What depends on it

[The first version](first-version.md).
