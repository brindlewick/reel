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

reel is on Android, iOS and the web from the start.

- **On phones, reel is a native app.** The app is a shell: the feed belongs to the app, and each
  game inside it is web code running in a web view.
- **On the web, the same games run in the browser.** What the web version is for, and how it
  works without a touch screen, is [a question of its own](web-version.md).

The cost the decision accepts: three platforms to build and test before the idea is known to
work.

## Why an app on phones

- A game on a phone is played in an app. A game in a phone browser is on a different platform,
  and reel is aimed at the first.
- The swipe is the heart of reel, and a browser handles it worst. There, a vertical swipe
  competes with the browser's own gestures: the address bar, pull-to-refresh and back
  navigation. An app owns every gesture on its screen.
- An app lifts limits a phone browser puts on a game, such as full screen, vibration and sound
  before the first touch (unverified: from memory, not yet captured).
- The game feeds that exist today mostly live inside apps and run web games there (unverified:
  from memory, not yet captured).

## What the web adds

The games are web code, so they run on the web as they are, and a link opens reel on any device
without an install. Keeping the games as web code also means one game runs on every platform,
and the catalog can change without an app update. Store rules allow an app to run HTML5 games it
downloads, under conditions (unverified: the current text has not been captured).

## Options that were considered

**The web alone, aimed at phone browsers.** One link works anywhere, and changes skip store
review. Not chosen: on phones, the browser takes over the swipe and limits the games, and a
phone game is expected to be an app.

**Native apps alone.** Chosen first, on 2026-09-27, and widened the same day to include the web.

**Native game code.** Not needed: nothing in the idea requires games to be native code, and store
rules make it hard for an app to download and run new native code, so the catalog could not
change freely (unverified: from memory, not yet captured).

## What would reopen it

Evidence that a feed of games in a phone browser feels as good as the same feed in the app, which
would make the apps optional. The test would be a side-by-side trial on one phone: the same feed
and games in the browser, added to the home screen, and inside the app, measuring the time from a
swipe to play, dropped frames, swipes the browser takes over and whether sound starts, and asking
a few people which they prefer without telling them which is which. No such trial is planned.

## What followed from it

- [Which phones first](mobile-os.md): Android and iOS both, answered by this decision.
- [The app shell](app-shell.md): how reel is built on all three platforms. Open.
- [The web version](web-version.md): what reel on the web is for. Open.

## What depends on it

[Game format](game-format.md), [swipe and game input](swipe-gesture.md),
[starting a game](game-start.md), [the app shell](app-shell.md),
[the web version](web-version.md) and [the first version](first-version.md).
