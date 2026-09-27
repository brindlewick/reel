---
title: The app shell
type: decision
status: open
updated: 2026-09-27
---

# The app shell

**Question.** How is the app built around the games? This has two parts: whether the feed itself
is native or a web page inside the app, and which framework the app is written in.

**Status: open.** This page holds a proposal. It follows from the [platform](platform.md)
decision.

## The feed: native, or a web page

**A native feed, with a web view for each game.** The app's own vertical pager moves between
games, with the phone's own scrolling. Each game runs in a web view of its own, apart from the
others. The swipe feels like the rest of the phone, and native code decides which touches go to
the feed and which to the game. The cost: the [message contract](game-format.md) passes through
each web view's bridge to native code.

**One web view, with the feed as a web page inside it.** The feed is a web page, and each game is
a frame in it. Almost all the code is web code, and it runs in a browser too. The cost: web code
still handles the swipe, only without the browser around it, so part of the reason for an app is
lost.

## The framework

**Swift for iOS and Kotlin for Android.** Full control and the most native feel, in two
codebases.

**React Native, with Expo.** One codebase in TypeScript, with a native pager and a web view for
each game. Expo's build service builds the iOS app in the cloud, so no Mac is needed
(unverified: not yet tried).

**Flutter.** One codebase in Dart, with its own pager and a web view plugin.

**Capacitor.** Wraps a web page in an app. It fits the one-web-view option, not a native feed.

## Recommendation

A native feed with a web view for each game, written in React Native with Expo. The swipe is
native, which is the reason for having an app. The code is TypeScript, and the iOS build needs
no Mac.

## What depends on it

[Game format](game-format.md), [swipe and game input](swipe-gesture.md),
[game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
