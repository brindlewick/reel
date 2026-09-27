---
title: Platform
type: decision
status: open
updated: 2026-09-25
---

# Platform

**Question.** Which platform does reel start on: the web in phone browsers, native apps, or
both?

**Status: open.**

## Options

**Web, aimed at phone browsers.** Each game runs in a sandboxed frame inside the page. One link
works on any phone or computer, and a change reaches players without a store review. The costs:
no app icon unless the player adds the page to their home screen, tighter browser limits on
sound, full screen and gestures than an app has, and players arrive through links rather than a
store.

**Native apps first, for iOS and Android.** A store listing, notifications and full control of
gestures. The costs: two apps or a cross-platform framework, a store review on every release,
and store rules on running code the app downloads after install. Apple's guidelines allow HTML5
mini games inside an app under conditions (unverified: the current text has not been captured).
The games themselves would most likely still be web code running in a web view.

**Both from the start.** Doubles the work before the idea is known to work.

## Recommendation

Web first. The first version has one question to answer, whether swiping to a new game feels
right, and a phone browser can answer it. A native app can later wrap the same feed in a web
view, and the games would carry over unchanged.

## What depends on it

[Game format](game-format.md), [swipe and game input](swipe-gesture.md) and
[the first version](first-version.md).
