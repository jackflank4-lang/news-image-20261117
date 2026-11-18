[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/jackflank4-lang/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/jackflank4-lang/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# World News — Tuesday 17 November 2026

A single 1024×1024 news poster summing up 17 November 2026's world news
in one image: the Kerch Bridge strike, Trump in Asia, the US losing measles
elimination status, the deepening Iran standoff, a wave of major outages,
Japan scrambling jets, Gaza, and protests in France — plus four smaller
items in the footer strip.

## How it was made

`poster.html` is the poster source: a single self-contained page
(1024×1024, system fonts only, no external assets, no network) with a dark
navy masthead, the date prominent at the top, and eight colour-coded story
blocks, each with a bold headline and a one-line summary. `entry.png` is a
screenshot of that page, rendered with headless Chromium.

## Running it

`main.py` (Python 3.13, stdlib only, no network) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Running it twice
produces byte-identical output.
