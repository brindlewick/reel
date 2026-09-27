---
title: The app shell
type: decision
status: open
updated: 2026-09-27
---

# The app shell

**Question.** How is reel built around the games on Android, iOS and the web? This has two parts:
whether the feed is native on phones or a web page everywhere, and which framework it is written
in.

**Status: open.** This page holds a proposal. It follows from the [platform](platform.md)
decision, and from [the web version](web-version.md) once that is decided.

## The feed: native on phones, or a web page everywhere

**Native on phones, web on the web.** On Android and iOS, the app's own vertical pager moves
between games with the phone's own scrolling, and each game runs in a web view of its own. On
the web, the feed is made of web elements, and each game runs in a frame. The swipe on phones
feels like the rest of the phone, which is the reason for having an app. The cost: the feed has
a phone form and a web form, and the [message contract](game-format.md) passes through a web
view's bridge on phones and through frame messages on the web.

**A web page everywhere.** The feed is one web page. On the web it runs as it is, and on phones
the app shows it in a single web view, with each game in a frame inside it. There is one form
for all three platforms. The cost: on phones, web code still handles the swipe, only without the
browser around it, so part of the reason for an app is lost.

## The framework

**React Native with Expo, including its web target.** One TypeScript codebase for Android, iOS
and the web. On phones it uses a native pager and a web view for each game. On the web it renders
to web elements, and each game runs in a frame. Expo's build service builds the iOS app in the
cloud, so no Mac is needed (unverified: not yet tried). How well a swipe feed works on Expo's web
target is unverified.

**Capacitor.** Wraps one web page in an app for each phone. It fits the web-page-everywhere
option and shares the most code, in TypeScript.

**Flutter.** One codebase in Dart for all three. Its web target draws the whole page itself,
which makes frames for games harder (unverified).

**Swift, Kotlin and a separate web feed.** Full control and the most native feel, in three
codebases.

## Recommendation

Native on phones and web on the web, in React Native with Expo. The swipe on phones is native,
which is the reason for the apps, and all three platforms share one TypeScript codebase. If
Expo's web target cannot give a good swipe feed, the web version can be a small web page of its
own that shares the games and the contract, without changing the apps.

## What depends on it

[Game format](game-format.md), [swipe and game input](swipe-gesture.md),
[game lifecycle](game-lifecycle.md) and [the first version](first-version.md).
