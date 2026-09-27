---
title: Game format
type: decision
status: open
updated: 2026-09-27
---

# Game format

**Question.** What does a game have to be to load into the feed?

**Status: open.** This page holds a proposal. It follows from the [platform](platform.md)
decision, and depends on [where games come from](game-sources.md) and
[the app shell](app-shell.md).

## Proposal

- **A static web bundle.** A folder with an `index.html` and its assets. It needs no server of
  its own.
- **One manifest entry per game**: an id, a title, a thumbnail, the entry URL, the orientation it
  expects, and whether it follows the contract. Nothing else until the feed needs it.
- **Isolated from the feed and from other games.** Each game runs where it cannot reach the feed
  or another game: in a web view of its own, or in a frame from a separate origin, depending on
  [the app shell](app-shell.md).
- **A small message contract.** The game tells the feed `ready` when it can start, and may
  report `score` or `ended`. The feed tells the game `pause`, `resume`, `mute` and `unmute`. A
  small script gives each game the same calls in the app and in a desktop browser, so a game can
  be built and tested in a browser.
- **A game that ignores the contract still runs.** The feed cannot pause it, so it unloads it
  when it leaves the screen.
- **A size limit on the first load**, set once [the first version](first-version.md) measures
  what a swipe can afford.

## Other options

**Native game code for each platform.** Set aside by the [platform](platform.md) decision: the
app is a shell for web games.

**One shared engine**, with each game as data and scripts for it. Games would be small and quick
to switch between. The costs: every game is tied to one engine, and no existing game fits.

## Recommendation

The static web bundle with the contract. It is what the app's web views run, a game can be built
and tested in an ordinary browser, each game is isolated from the feed and from the other games,
and an existing web game fits with at most a small adapter.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
