---
title: Where games come from
type: decision
status: open
updated: 2026-09-25
---

# Where games come from

**Question.** Where do the games in the feed come from? Two answers are needed: one for the
first version, and the long-run aim, since the aim shapes the design earlier than it seems.

**Status: open.**

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

## Recommendation

In-house for the first version. It removes every question except the one being tested.

For the long run, decide the aim now even though it is not built yet. Uploads need games served
from an isolated origin, and review and moderation from the start. Curated games need licensing,
and a way to handle games that ignore the contract.

## What depends on it

[Game format](game-format.md), [game length](game-length.md) and
[the first version](first-version.md).
