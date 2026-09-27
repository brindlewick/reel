---
title: Where games come from
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Where games come from

**Question.** Where do the games in the feed come from? Two answers are needed: one for the
first version, and the long-run aim, since the aim shapes the design earlier than it seems.

**Status: decided on 2026-09-27 for the first version.** The long-run aim is still open.

## Options

**Written in-house.** Every game is built for the feed: a portrait screen, touch input, a small
download and the [message contract](game-format.md). The cost: the catalog grows only as fast as
the project writes games.

**Curated games by other authors.** Many web games exist. The costs: a license for each one, and
most were not made for a portrait phone screen or to pause when asked. Their authors would have
to adopt the contract, or the feed would have to treat their games as ones it cannot pause.

**Uploads from creators.** The catalog grows by itself. The costs: hosting, review before a game
goes live, moderation, and handling abuse, since a game is code running on a player's phone,
even inside a sandbox. This makes reel a platform as well as a feed.

## Decision

In-house for the first version. It removes every question except the one being tested.

## Still open

The long-run aim: games written in-house only, curated games by other authors, or uploads from
creators. It is worth deciding before the design hardens. Uploads need games served from an
isolated origin, and review and moderation from the start. Curated games need licensing, and a
way to handle games that ignore the contract.

## What would reopen it

Nothing in the first version. The long-run aim, once decided, may add other sources beside
in-house games.

## What depends on it

[Game format](game-format.md), [game length](game-length.md) and
[the first version](first-version.md).
