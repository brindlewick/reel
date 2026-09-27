---
title: Game format
type: decision
status: open
updated: 2026-09-25
---

# Game format

**Question.** What does a game have to be to load into the feed?

**Status: open.** This page holds a proposal. It depends on the [platform](platform.md) and on
[where games come from](game-sources.md).

## Proposal

- **A static web bundle.** A folder with an `index.html` and its assets. It needs no server of
  its own.
- **One manifest entry per game**: an id, a title, a thumbnail, the entry URL, the orientation it
  expects, and whether it follows the contract. Nothing else until the feed needs it.
- **A sandboxed frame on a separate origin.** The game runs in an iframe served from a different
  origin from the feed, so it cannot read the feed's storage or take over the page.
- **A small message contract** over `postMessage`. The game tells the feed `ready` when it can
  start, and may report `score` or `ended`. The feed tells the game `pause`, `resume`, `mute`
  and `unmute`.
- **A game that ignores the contract still runs.** The feed cannot pause it, so it unloads it
  when it leaves the screen.
- **A size limit on the first load**, set once [the first version](first-version.md) measures
  what a swipe can afford.

## Other options

**Native game code for each platform.** Rules out the web, and store rules limit code an app
downloads.

**One shared engine**, with each game as data and scripts for it. Games would be small and quick
to switch between. The costs: every game is tied to one engine, and no existing game fits.

## Recommendation

The static web bundle with the contract. It runs in any browser and in a native web view, each
game is isolated from the feed and from the other games, and an existing web game fits with at
most a small adapter.

## What depends on it

[Game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
