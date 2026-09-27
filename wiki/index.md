---
title: reel wiki
type: schema
updated: 2026-09-27
---

# reel wiki

What reel has decided and what it knows. reel is a feed of playable games: one game on screen at
a time, and a swipe moves to a different one.

A decision is **open** until the user answers it, then **decided**. A concept is a claim about
how something really behaves, with a standing from **claimed** to **settled**, and it cites the
evidence it rests on in [`raw/`](../raw/README.md). [How the wiki is kept](schema.md) defines
both, and [the log](log.md) lists every change.

## Decisions

- [Platform](decisions/platform.md): **decided**. Android, iOS and the web from the start. On
  phones, a native app that is a shell for web games.
- [Which phones first](decisions/mobile-os.md): **decided**. Android and iOS, both from the
  start, and what that costs.
- [The app shell](decisions/app-shell.md): **decided**. A native pager with a web view per game
  on phones, and a web feed with a frame per game on the web, in React Native with Expo.
- [The web version](decisions/web-version.md): **decided**. The full feed on every device. On a
  computer, the wheel, a trackpad and the arrow keys move between games.
- [Where games come from](decisions/game-sources.md): **decided**. Written in-house for the first
  version. The long-run aim is still open.
- [Game format](decisions/game-format.md): **decided**. A static web bundle, isolated from the
  feed and from other games, with a manifest entry and a small message contract.
- [Swipe and game input](decisions/swipe-gesture.md): **decided**. A swipe anywhere moves the
  feed, and the first games leave vertical swipes alone.
- [Starting a game](decisions/game-start.md): **decided**. A game waits on its own start screen
  and starts on the first touch. Sound starts with play.
- [Coming back to a game](decisions/game-return.md): **decided**. Only the game just left
  resumes. Anything further back starts fresh.
- [Game lifecycle](decisions/game-lifecycle.md): **decided**. A live window of three games, one
  active game, and the states a game passes through.
- [Game length](decisions/game-length.md): **decided**. Short loops, with a round under a minute.
- [Feed order](decisions/feed-order.md): **decided**. A fixed order for the first version, then a
  shuffle. Whether recommendations are part of the core idea is still open.
- [The first version](decisions/first-version.md): **decided**. Four small games in a feed on
  Android, iOS and the web, and five measures of whether swiping to a new game works. Which
  phones the trials run on is still open.

## Concepts

How phones, browsers, web views and app stores really behave, as distinct from what their
documentation says. None yet. Claims the decisions rest on are marked unverified until a trial backs them.

## Sources

Documentation and articles captured as evidence. None yet.

## About the wiki

- [How the wiki is kept](schema.md): page kinds, statuses, standings, citations and the check.
- [Log](log.md): every change to the wiki, newest first.
