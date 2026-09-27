---
title: Game format
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Game format

**Question.** What does a game have to be to load into the feed?

**Status: decided on 2026-09-27.** It follows from the [platform](platform.md),
[where games come from](game-sources.md) and [app shell](app-shell.md) decisions.

## Decision

- **A static web bundle.** A folder with an `index.html` and its assets. It needs no server of
  its own.
- **One manifest entry per game**: an id, a title, a thumbnail, the entry URL, the orientation it
  expects, and whether it follows the contract. Nothing else until the feed needs it.
- **Isolated from the feed and from other games.** Each game runs where it cannot reach the feed
  or another game: in a web view of its own, or in a frame from a separate origin, depending on
  [the app shell](app-shell.md).
- **A small message contract.** The game tells the feed `ready` when it can start, and may
  report `score` or `ended`. The feed tells the game `pause`, `resume`, `mute` and `unmute`. A
  small script gives each game the same calls in the apps and on the web, so a game is written
  once and can be built and tested in a browser.
- **A game that ignores the contract still runs.** The feed cannot pause it, so it unloads it
  when it leaves the screen.
- **A size limit on the first load**, set once [the first version](first-version.md) measures
  what a swipe can afford.

## Other options

**Native game code for each platform.** Set aside by the [platform](platform.md) decision: the
apps are shells for web games.

**One shared engine**, with each game as data and scripts for it. Games would be small and quick
to switch between. The costs: every game is tied to one engine, and no existing game fits.

## Why

The same bundle runs in the apps' web views and on the web, a game can be built and tested in an
ordinary browser, each game is isolated from the feed and from the other games, and an existing
web game fits with at most a small adapter.

## What would reopen it

Games by other authors that cannot adopt the contract, or a first-load size limit that no game
can meet.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
