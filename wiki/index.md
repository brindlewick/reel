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

- [Platform](decisions/platform.md): **decided**. A native app from the start, as a shell that
  runs web games.
- [Which phones first](decisions/mobile-os.md): **open**. iOS, Android or both.
- [The app shell](decisions/app-shell.md): **open**. How the app is built around the games: a
  native feed or a web page inside the app, and which framework.
- [Where games come from](decisions/game-sources.md): **open**. Games written in-house, curated
  games by other authors, or uploads from creators, now and in the long run.
- [Game format](decisions/game-format.md): **open**. What a game has to be to load into the
  feed. Proposed: a static web bundle, isolated from the feed and from other games, with a
  manifest entry and a small message contract.
- [Swipe and game input](decisions/swipe-gesture.md): **open**. How a swipe to another game is
  told apart from a game's own touch input.
- [Starting a game](decisions/game-start.md): **open**. Whether a game plays as soon as it is on
  screen or waits for the player, and when sound starts.
- [Coming back to a game](decisions/game-return.md): **open**. Whether a game the player swipes
  back to resumes where it was left or starts fresh.
- [Game lifecycle](decisions/game-lifecycle.md): **open**. How games are loaded, run, paused and
  unloaded as they scroll in and out of view.
- [Game length](decisions/game-length.md): **open**. Short loops made for the feed, or any game.
- [Feed order](decisions/feed-order.md): **open**. What decides which game comes next: a fixed
  order, a shuffle or recommendations.
- [The first version](decisions/first-version.md): **open**. The smallest build that shows
  whether swiping to a new game works, and how to tell.

## Concepts

How phones, web views and app stores really behave, as distinct from what their documentation
says. None yet. Claims the decisions rest on are marked unverified until a trial backs them.

## Sources

Documentation and articles captured as evidence. None yet.

## About the wiki

- [How the wiki is kept](schema.md): page kinds, statuses, standings, citations and the check.
- [Log](log.md): every change to the wiki, newest first.
