# Cinny: what it is and what it does

*Product overview, written 8 October 2026 by Codesquare AB*

Cinny is a movie and TV tracker for iPhone and Android. You log what you watch, rate it, build watchlists, swipe through a fresh deck of picks every night, and see what the people you follow are watching. Films and series live in one diary, in the order you watched them.

> **Track every movie. Never forget a show.**

## Contents

1. [At a glance](#at-a-glance)
2. [How Cinny works](#how-cinny-works)
3. [Onboarding](#onboarding)
4. [The swipe deck](#the-swipe-deck)
5. [Home and recommendations](#home-and-recommendations)
6. [Search and title pages](#search-and-title-pages)
7. [Logging and rating](#logging-and-rating)
8. [Watchlists and timeline](#watchlists-and-timeline)
9. [Social](#social)
10. [Where to watch](#where-to-watch)
11. [Profile and stats](#profile-and-stats)
12. [Notifications](#notifications)
13. [Privacy and account](#privacy-and-account)
14. [Cinny Plus](#cinny-plus)
15. [Example pricing](#example-pricing)
16. [Market](#market)
17. [Data and partners](#data-and-partners)
18. [Technology](#technology)
19. [Status and open items](#status-and-open-items)

## At a glance

| | |
|---|---|
| **Product** | Movie and TV tracker with swipe discovery |
| **Platforms** | iOS and Android app; marketing website at cinny.app |
| **Status** | Pre-launch, v1.0.0 in store review |
| **Business model** | Freemium: free core, paid Cinny Plus |
| **Audience** | Heavy watchers aged about 18–35 |
| **Company** | Codesquare AB, Sweden |
| **App language** | English; store listings in 11 languages |
| **Brand colour** | `#E50914` red on black |

### Positioning

Most trackers make you pick a side. Letterboxd is built for films, while Trakt and the now-closed TV Time lean towards series. Cinny tracks both in one place. Two features set it apart from those apps: a nightly swipe deck that teaches the recommender your taste, and recommendations that come from people you follow.

The store listing title is **Cinny: Movie & TV Tracker**, and the subtitle is **Swipe to find what to watch**.

## How Cinny works

The app is built around one loop. Each step feeds the next.

1. **Taste.** Pick genres and a few favourites. Picks start straight away, before you even sign up.
2. **Swipe.** A fresh deck every night. Each verdict sharpens your taste profile.
3. **Discover.** Home shelves, For You and "Because you watched" picks ranked to your taste.
4. **Log.** Diary entries with date, rating and review, for films and seasons.
5. **Share.** Followers see your activity; you see theirs.

The app has four tabs: **Home**, **Swipe**, **Lists** and **Activity**. Search is always available, and your profile opens from the avatar in each tab's header.

## Onboarding

- **Try before signing up.** Pick genres you love and a few titles you've loved, and Cinny shows about 12 recommendations right away. You can add any of them to your watchlist before creating an account.
- **Sign in** with email and password, Google, or Apple. Email sign-ups confirm a 6-digit code. Every method that uses the same verified email opens the same account.
- **Username:** 3–24 characters (lowercase letters, digits, underscores), changeable once every 30 days.
- **Age:** users must be 13 or older.
- The flow ends with an analytics consent screen ("Help make Cinny better") and a prompt to turn on notifications.
- Your taste profile can be edited later. You can also **mute genres** so they never show up in recommendations, though they still appear in search.

## The swipe deck

The Swipe tab deals you one title at a time, ranked by your taste with a mix of popular titles and a small share of wildcards. You judge each card in one of four ways:

| Action | Meaning | Where it goes |
|---|---|---|
| Swipe right | Interested | A private "swipe inbox" list |
| Swipe left | Not interested | Hidden for a while (see below) |
| Swipe up | Already watched | A diary entry, with optional date, rating and comment |
| Watchlist button | Want to watch | A list you choose |

- **Undo** takes back the last swipe. A filter switches between All, Movies and Series.
- **Daily allowance:** free users get **20 swipes per day**. The day resets at 03:00 local time, so a late-night session doesn't use up tomorrow's deck. When the deck runs out you see "That's today's last swipe" and the time more swipes arrive. Cinny Plus removes the limit.
- **Not interested cools down.** A rejected title comes back after 96 hours, then 14 days, then 60 days. After a fourth rejection it's gone for good. Any positive swipe resets this.
- The deck skips anything you've watched, already saved, or that's currently at the top of Home.
- A hidden safety limit (60 swipes a minute) blocks scripts. People never hit it.

## Home and recommendations

Home is a stack of shelves, in this order. A shelf with nothing to show hides itself.

1. **Hero:** three popular titles, re-ordered to your taste.
2. **Top 10 Today.**
3. **For You:** ranked purely on your taste.
4. **Popular among people you follow.**
5. **Because you watched X:** based on something you watched in the last 30 days and didn't rate below 6.
6. **New Releases:** new movies, new series and new seasons.
7. **Popular on Cinny:** what Cinny users watched and saved most in the last 30 days.
8. **New seasons:** new and upcoming seasons of shows you've watched and liked ("Coming Nov 26").

The recommender builds a taste profile from your favourites, your diary, your ratings and your swipes. In offline tests on development accounts, the current recommender found the right title in its top 20 more than four times as often as the version before it.

## Search and title pages

### Search

- Every film and series in TMDB is searchable live. Tabs: All, Movies, Series, Cast & Crew.
- Before you type, you see recent searches and 12 genre tiles to browse. Browsing can be sorted by Popular, Top rated or Newest, and filtered by genre, runtime, rating, decade, or by hiding what you've watched.
- **Person pages** show an actor's or director's filmography and how much of it you've seen ("16 of 50 watched · 32%").
- Other Cinny users can be found by username.

### Title pages

- Info, **Where to watch**, seasons, cast, director or creator, trailers and alternate images.
- **People you follow:** who watched it and who wants to ("Maja and Oskar watched this"). Their ratings are never shown here.
- **Reviews** in three tabs: Public, Following and Mine. Spoilers stay hidden until you tap to reveal them. Season reviews appear here too.
- A Share button. Shared links open a landing page on cinny.app that points people to the app.

## Logging and rating

- Every watch is a **diary entry** with a date (backdating is allowed), an optional rating from 1 to 10, an optional review with a spoiler flag, a rewatch flag and its own visibility.
- Rewatches get their own entries and ratings. **Your rating** for a title is the one from your most recent watch, so logging an old viewing never overwrites your current opinion.
- You can only rate something after logging it, and you can't log a title that hasn't been released yet. You can still add unreleased titles to a watchlist.
- **Seasons** can be logged and rated one by one. A season's rating never changes the show's rating.
- Community averages count one vote per person.

## Watchlists and timeline

- **Watchlist:** your default list. You can rename it and set who sees it.
- **Swipe inbox:** a private list of everything you swiped right on. A title leaves it automatically when you save it to another list.
- **Custom lists:** 5 for free users, 100 with Cinny Plus. A title can sit on several lists at once.
- **Sorting and filtering are free:** drag to reorder, sort by date added, title, year, rating or runtime, and filter by type, genre, runtime, rating or decade, or hide watched titles. **Pick for me** chooses a random title from the list.
- **Collaborative lists** (Cinny Plus): invite people you follow as editors or viewers. Members don't need Cinny Plus themselves.
- **My Timeline** shows every entry in watch-date order, grouped by month, with filters for movies or series, rated, reviewed, and a year picker.

## Social

- **Following is one-way**, like Instagram. You can follow a public profile instantly. A private profile has to approve your request first.
- The **Activity** tab shows what people you follow logged and saved, grouped so it stays readable ("watched 4 seasons of The Wire", "added 6 titles to Horror Night"). A filter narrows it to mutuals.
- **Taste match:** a 0–100 score for how closely your taste lines up with another user's.
- **Safety tools:**
  - **Block** removes the follow in both directions and hides you from each other.
  - **Mute** quietly hides someone from your feed and shelves.
  - **Report** covers users and reviews.

## Where to watch

- **Free:** every title page shows where it streams, rents or sells in your country, with a link to the full list on TMDB. The data is powered by JustWatch.
- **Cinny Plus — My streaming services:** choose the services you pay for. They're ranked first on title pages, and your lists get an "On my services" filter with a count per service. The count shows which service would cover the most of your watchlist if you subscribed for a month.
- **Planned:** alerts when a watchlisted title arrives on your services, and a "Popular on your services" shelf.

## Profile and stats

### Profile

- Three numbers (Watched, Followers, Following), a bio, **3 favourite titles** for everyone, and tabs for activity and watchlists.
- **Cinny Plus customisation:** a profile backdrop from any title, alternate posters on favourites, a custom poster on reviews, and a gold Plus badge.

### Personal stats

Only you can see your stats. Pick a year or All time. The screen fills in after 10 logged entries.

| Free | Cinny Plus |
|---|---|
| Hours watched | Year vs year |
| Movies and series watched | Watch time by month |
| Top genre | Weekday pattern |
| Swipes and reviews written | Genre breakdown |
| Watch time split into series and movies | Records (longest, shortest, oldest) |
| Viewing activity heatmap (tap a period to see what you watched) | Rating distribution and average |
| | Top 5 highest rated |
| | Most-watched titles, actors and directors |
| | Swipe breakdown and busiest swipe hour |

Planned: a yearly **Wrapped** recap in December with shareable story slides. It will be free for everyone.

## Notifications

In-app notifications cover new followers, follow requests and list invites. Push notifications come in categories you can each turn off, and they're timed to your local clock:

| Push | When | Example |
|---|---|---|
| Activity digest | Sunday 18:00 | "Anna watched Stranger Things, Bram watched Dune, +6 more" |
| Swipe reminder | 19:00 | Sent only if you haven't swiped today |
| New season | 19:00 | "New seasons: Severance and 2 more" |
| Rating reminder | 20:00 the next day | "You watched Dune — rate it?" |

Cinny never sends a push for every single thing someone you follow watches.

## Privacy and account

- **Profiles are public by default.** A private profile is visible only to followers you approve. Each entry and list can also be set to follow your profile setting, followers only, or private.
- Private entries still count anonymously towards averages and recommendations, but they're never shown with your name.
- **Analytics are opt-in.** Nothing is collected until you agree, data is never linked to your account, and there's no session recording. You can change your answer in Settings.
- **Deleting your account** works from the app or from cinny.app/delete-account. You confirm through a single-use email link that expires after 5 minutes, and deletion happens immediately and completely.
- Codesquare AB is the data controller under GDPR, Swedish law applies, and Cinny does not sell personal data.

## Cinny Plus

Cinny is freemium. Everything you need to track, rate, list and follow is free and has no caps. Cinny Plus is a single paid tier on top, built around three things: unlimited discovery, more control, and deeper insight into your own viewing.

> **Naming:** the app currently calls the tier **"Cinny Premium"** (for example "More lists with Cinny Premium"). This document uses "Cinny Plus". If that's the name going forward, the in-app copy needs updating too.

| Feature | Free | Cinny Plus |
|---|---|---|
| Logging, ratings, reviews, history | Unlimited | Unlimited |
| Swipe deck | 20 per day | Unlimited |
| Custom lists | 5 | 100 |
| Collaborative lists | Can join as a member | Create and invite |
| List sorting, filters, Pick for me | Yes | Yes |
| Where to watch | Yes | Yes |
| My streaming services and "On my services" filter | — | Yes |
| Personal stats | Core set + heatmap | Every stat |
| Favourites | 3 | 3 |
| Profile backdrop, custom posters, badge | — | Yes |
| Following, activity, notifications | Yes | Yes |
| Ads (planned for free users) | Yes, once ads launch | None |

### Rules

- **Lapsing locks features but never deletes anything.**
  - Lists stay editable.
  - Collaboration pauses, so editors become viewers.
  - Backdrops, posters and the badge are hidden but saved, and they come back if you resubscribe.
- Purchases happen **only in the iOS and Android apps**, through the App Store and Google Play. The website doesn't sell anything.
- Free users see locked Plus features with their names visible, so they know what they'd get. The places that prompt an upgrade are:
  - the 20-swipe wall
  - creating a 6th list
  - tapping a locked stat
  - opening the streaming-services picker

## Example pricing

> **These are proposals, not decisions.** They come from the pricing strategy draft ([pricing/pricing-strategy.md](pricing/pricing-strategy.md), 2 October 2026). No prices are final yet, and the paywall isn't built.

| Plan | Price | What you get |
|---|---|---|
| Free | $0 | Unlimited tracking, 20 swipes a day, 5 lists, where to watch, core stats |
| Plus, monthly | $3.99/mo | Everything in Plus, billed monthly. Shown first as the price anchor |
| **Plus, annual** | **$24.99/yr** | About $2.08 a month, 48% less than paying monthly. Selected by default, with a 7-day free trial |
| Lifetime | $79.99 once | Pay once and keep Plus for good, with a "Founder" badge and early access to new Plus features |

### Launch offer (first 90 days)

- Annual: **$14.99 for the first year**, then $24.99. That's below Letterboxd Pro, to win switchers from TV Time and Trakt.
- Lifetime: **$59.99**. Monthly stays at $3.99.
- Early subscribers keep their price for as long as they stay subscribed.

### Unit economics (estimates)

| Plan | Price | Net after 15% store fee | Net per month |
|---|---|---|---|
| Monthly | $3.99 | $3.39 | $3.39 |
| Annual | $24.99 | $21.24 | $1.77 |
| Lifetime | $79.99 | $67.99 | $1.89 over 3 years |

- Fixed costs are about **$110 a month** (hosting plus the Apple developer fee). Each active user costs about **$0.02 a month**.
- To break even: about **33 monthly** or **62 annual** subscribers.
- Assuming 70% annual, 25% monthly and 5% lifetime, each paying user brings in about **$2.18 net a month**. At 3% conversion, free users pay for themselves before any ad revenue.
- The biggest unknown is TMDB's fee once revenue passes a few hundred dollars. Get that number in writing before launch.

### When to raise prices

Any one of these triggers a review:

- more than 40% of trials converting to paid
- the launch of watchlist arrival alerts or imports from other apps
- more than 1,000 paying users (enough for an A/B test of $24.99 against $29.99)
- the TMDB fee pushing margins below 80%

Raise prices by at most 20% at a time and announce it 30 days ahead. Separately, if more than 30% of daily users hit the 20-swipe wall, raise the free limit to 30.

## Market

| Competitor | Paid tier | Cinny's position |
|---|---|---|
| Letterboxd | Pro $18.99/yr · Patron $48.99/yr | Films only. Cinny Plus sits between Pro and Patron and also includes Patron's cosmetics |
| Trakt | VIP $5.99/mo · $59.99/yr | Well below. Its users called the price "wild", which makes them a good pool to win over |
| Sequel | $2.99/mo · $19.99/yr · $99.99 lifetime | Close on price. Cinny gives where to watch away for free |
| Simkl | ~$70/yr | Different audience (anime and power users) |
| TV Time | — | Shut down 15 July 2026, so its users need a new home |

Competitor prices were collected on 1 October 2026.

## Data and partners

- **TMDB** supplies all title, person and image data. Cinny keeps its own copy and refreshes it nightly. Required credit: "This product uses the TMDB API but is not endorsed or certified by TMDB." Under the current agreement the API is free until revenue reaches a few hundred dollars.
- **JustWatch** supplies streaming availability through TMDB and must be credited wherever that data appears. Affiliate links would need a JustWatch partner agreement.
- **PostHog** (EU-hosted) runs analytics, and only with consent. On iOS, Apple's tracking prompt asks for that consent.
- Other services:
  - **Resend** for email
  - **Expo** for push notifications
  - **Railway** for hosting
  - **Better Auth** for sign-in
  - **RevenueCat** (planned) for subscriptions

## Technology

- **Mobile:** React Native with Expo, from one codebase for iOS and Android. A dark-only design.
- **Backend:** TypeScript with Hono, oRPC and Effect. PostgreSQL with Drizzle, and pgvector for taste embeddings.
- **Recommender:** a separate service that ranks titles against your taste profile.
- **Scheduled jobs:** nightly catalog refreshes and push notifications.
- **Website:** Next.js. It covers marketing, the FAQ, legal pages, contact, account deletion and shared-title landing pages.
- Everything lives in one pnpm and Turborepo monorepo.

## Status and open items

- **Pre-launch.** Version 1.0.0 is in App Store review, and the store links will work once the listing goes public.
- **Cinny Plus is built but can't be bought yet.** The gates and features are in place. The paywall and the RevenueCat connection are the last big pieces, after which ads come in. Until then, Plus can only be switched on by hand.
- **No prices are final.** The figures above are examples from the draft strategy.
- **Not built yet:**
  - importing from other trackers
  - a release calendar
  - watchlist arrival alerts
  - Wrapped
  - the web journal
- **Copy to fix:**
  - Parts of the website say "swipe right to add it to your watchlist", but a right swipe goes to the swipe inbox.
  - "When the deck runs out, that's the night" is only true for free users.
  - The in-app name "Cinny Premium" doesn't match "Cinny Plus".

---

*Compiled from the Cinny repository (core domain glossary, ADRs, marketing copy, store listings and the pricing strategy draft) on 8 October 2026. Prices shown are examples and not final.*
