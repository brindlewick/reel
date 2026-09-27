---
title: Game lifecycle
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Game lifecycle

**Question.** How is a game loaded, run, paused and unloaded as it scrolls in and out of view?

**Status: decided on 2026-09-27.** It follows from [starting a game](game-start.md),
[coming back to a game](game-return.md), [swipe and game input](swipe-gesture.md) and
[the app shell](app-shell.md).

## Decision

**A live window of three games**: the one on screen, the one before it and the one after it.
Anything further away is removed, and loaded again if the player comes back to it.

**One active game.** A game becomes active when most of it is on screen and the scroll has come
to rest. Only the active game gets touch input and sound. When a game stops being active, the
feed sends it `pause` and mutes it.

**A game passes through these states:**

| state | what it means |
|---|---|
| unloaded | outside the live window. Nothing is loaded. |
| loading | inside the window, and its web view or frame is loading |
| ready | loaded, and it has sent `ready` if it follows the contract |
| active | on screen, with touch input and sound |
| paused | inside the window but off screen, and still loaded |
| failed | it did not become ready in time. The feed says so and lets the player move on. |

A game that does not follow the [contract](game-format.md) cannot be paused. It is unloaded when
it leaves the screen, so it starts fresh when the player comes back to it.

**Three is a guess.** Whether a mid-range phone keeps three games running without stutter, in the
app or in a browser, is unverified, and [the first version](first-version.md) measures it.

## What would reopen it

The first version's measurements. If three live games stutter on a mid-range phone, the window
shrinks. If there is room to spare, it may grow.

## What depends on it

[The first version](first-version.md).
