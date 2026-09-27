---
title: Platform
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Platform

**Question.** Which platform does reel start on: the web in phone browsers, native apps, or
both?

**Status: decided on 2026-09-27.**

## Decision

reel is a native app from the start. The app is a shell: the feed belongs to the app, and each
game inside it is web code running in a web view.

## Why

- A game on a phone is played in an app. A game in a phone browser is on a different platform,
  and reel is aimed at the first.
- The swipe is the heart of reel, and a browser handles it worst. There, a vertical swipe
  competes with the browser's own gestures: the address bar, pull-to-refresh and back
  navigation. An app owns every gesture on its screen.
- An app lifts limits a phone browser puts on a game, such as full screen, vibration and sound
  before the first touch (unverified: from memory, not yet captured).
- The game feeds that exist today mostly live inside apps and run web games there (unverified:
  from memory, not yet captured).

Keeping the games as web code keeps what the web offered: one game runs on every phone, and the
catalog can change without an app update. Store rules allow an app to run HTML5 games it
downloads, under conditions (unverified: the current text has not been captured).

## Options that were considered

**Web, aimed at phone browsers.** One link works anywhere, and changes skip store review. Not
chosen: the browser takes over the swipe and limits the games, and a phone game is expected to
be an app.

**A native app with native game code.** Not needed: nothing in the idea requires games to be
native code, and store rules make it hard for an app to download and run new native code, so the
catalog could not change freely (unverified: from memory, not yet captured).

**Both web and native from the start.** Doubles the work before the idea is known to work.

## What would reopen it

Evidence that a feed of games in a phone browser feels as good as the same feed in the app. The
test would be a side-by-side trial on one phone: the same feed and games in the browser, added to
the home screen, and inside the app, measuring the time from a swipe to play, dropped frames,
swipes the browser takes over and whether sound starts, and asking a few people which they
prefer without telling them which is which. No such trial is planned.

## Still open

- [Which phones first](mobile-os.md): iOS, Android or both.
- [The app shell](app-shell.md): how the app is built around the games.

## What depends on it

[Game format](game-format.md), [swipe and game input](swipe-gesture.md),
[starting a game](game-start.md), [the app shell](app-shell.md) and
[the first version](first-version.md).
