---
title: Which phones first
type: decision
status: decided
decided: 2026-09-27
updated: 2026-09-27
---

# Which phones first

**Question.** Does the app start on iOS, on Android, or on both?

**Status: decided on 2026-09-27.**

## Decision

Both. reel is on Android and iOS from the start, alongside the web, as the
[platform](platform.md) decision says.

## What it costs

- An iOS app is built on a Mac or by a macOS build service.
- Putting test builds on other people's iPhones needs a paid Apple developer account.
- An Android test build installs straight from a file, with no store and no account, but there
  are many phones and screen sizes to check.
- Testing and store work happen on two platforms before the idea is known to work.

A cross-platform framework keeps most of the app in one codebase. See
[the app shell](app-shell.md).

## Options that were considered

**iOS first** and **Android first**, each putting off the other platform's costs until the idea
works. Not chosen: reel is multi-platform from the start.

## What would reopen it

A cost on one platform that holds the first version back, such as an iOS build that cannot be set
up.

## What depends on it

[The app shell](app-shell.md) and [the first version](first-version.md).
