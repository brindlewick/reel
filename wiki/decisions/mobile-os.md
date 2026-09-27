---
title: Which phones first
type: decision
status: open
updated: 2026-09-27
---

# Which phones first

**Question.** Does the app start on iOS, on Android, or on both?

**Status: open.** It follows from the [platform](platform.md) decision.

## Options

**iOS first.** The costs: an iOS app is built on a Mac or by a macOS build service, and putting
test builds on other people's phones needs a paid Apple developer account.

**Android first.** An Android app builds on any operating system, and a test build installs
straight from a file, with no store and no account. The cost: many phones and screen sizes to
check.

**Both from the start.** With a cross-platform framework, most of the app is written once (see
[the app shell](app-shell.md)). The cost: testing and store work on two platforms before the idea
is known to work.

## Recommendation

Whichever phones are at hand for testing, since [the first version](first-version.md) is judged
on a real phone. With a cross-platform framework, the other platform can follow at a low cost
once the first works.

## What depends on it

[The app shell](app-shell.md) and [the first version](first-version.md).
