---
title: The web version
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# The web version

**Question.** What is reel on the web for, and how does it work without a touch screen?

**Status: decided on 2026-09-27.** It follows from the [platform](platform.md) decision, which
puts reel on the web as well as on phones.

## Why it matters

On a computer there is no touch. The swipe between games, and the taps inside them, need a
mouse, a trackpad or a keyboard instead. In a phone browser, a swipe competes with the browser's
own gestures, which is one of the reasons reel is an app on phones.

## Options

**The full feed, on every device.** The same feed on a computer and in a phone browser. On a
computer, the scroll wheel, a trackpad swipe and the arrow keys move between games, and a click
stands in for a tap. The costs: every game must also work with a mouse, which is easy for games
played with taps and harder for games built on drags, and in a phone browser the swipe is at its
weakest.

**The full feed on computers, and the app on phones.** A phone browser shows the game a link
points to, with a way to get the app for the rest of the feed. The costs: two web experiences to
design, and a player on a phone has to install the app to swipe.

**Shared links only.** On any device, the web shows the one game a link points to, and invites
the player to the app for the feed. The least work, but the web is not a feed.

## Decision

The full feed on every device for the first version. It has one behaviour to define and test,
and it is also where games are built and tried out. Whether a phone browser should point to the
app can wait until the apps are in the stores.

## What would reopen it

The apps reaching the stores, when the question of pointing phone browsers to the app comes
back, or games that cannot be played well with a mouse.

## What depends on it

[The app shell](app-shell.md), [swipe and game input](swipe-gesture.md) and
[the first version](first-version.md).
