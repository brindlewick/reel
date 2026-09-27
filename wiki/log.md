---
title: Log
type: schema
updated: 2026-09-27
---

# Log

Append-only. Newest first. One entry per operation, headed `## [YYYY-MM-DD] <operation> | <title>`.

## [2026-09-27] decide | platform widened to Android, iOS and the web

The platform decision is widened: reel is on Android, iOS and the web from the start. On phones
it stays a native app that is a shell for web games. The same answer settles which phones first:
Android and iOS, both from the start. One new open question follows: what the web version is
for, and how it works without a touch screen. The app shell's recommendation now covers all
three platforms: native on phones and web on the web, in one TypeScript codebase. The open pages
now cover the web as well as the apps.

## [2026-09-27] decide | platform: a native app that runs web games

reel is a native app from the start, and the app is a shell for games written as web code. The
reasons are on the page, and the claims they rest on are marked unverified. Two open questions
follow from it: which phones first, and how the app shell is built. The open pages that assumed a
browser now assume the app: game format, swipe and game input, starting a game, game lifecycle
and the first version. Starting a game now says when sound should start, since in an app it could
start without a touch. The recommendation is that it starts when play starts.

## [2026-09-25] create | wiki started

The wiki starts with ten open decisions from the first design proposal: platform, where games
come from, game format, swipe and game input, starting a game, coming back to a game, game
lifecycle, game length, feed order and the first version. Each lists its options and a
recommendation. None is decided. There are no concepts or sources yet. Claims the decisions rest
on are marked unverified until a trial or a captured source backs them.
