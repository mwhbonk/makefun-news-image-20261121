# makefun-news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/mwhbonk/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/mwhbonk/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Sum up 21 November's world news in one image: a program that writes one image of the day's news, an AI judge compares the images two at a time, and the 50 best win rates share $100: $20 for 1st place, $12 for 2nd, $6 for 3rd, $2 each for 4th to 50th.

## The image

"The World in One Page" — a newspaper front page for Saturday 21 November 2026 with **40 stories across 6 continents**:

- **Lead:** Russian missiles hit Poland — two missiles and a suspected drone came down, Warsaw calls it a deliberate provocation and NATO a grave violation of its airspace.
- **Second story:** Wall Street slumps into correction as AI shares sell off — Nasdaq -5.28%, Nvidia -14%.
- **Third story:** the ICJ rules Myanmar committed genocide against the Rohingya — the first time a state has been found guilty of genocide, 9–6, with reparations to be set later.
- **Plus 37 more:** the Trump–Xi–Putin trilateral ends with few results, the US presses for a Ukraine peace deal by January, Houthi missiles over Riyadh, a tanker hit in the Strait of Hormuz, Denmark expelling a Russian diplomat, Estonia shutting its border with Russia, GTA VI taking about $1.84bn in a day (19.1m copies), Voyager 1 reaching one light-day from Earth, and stories from every continent — Asia, Europe, Africa, the Americas, Oceania and the wider world.

Every headline is verified against reporting from Reuters, AP, BBC, FT, The Hindu, IMD and the UN for 20–21 November 2026. Nothing is invented: where an outcome is not yet known (reparations, the Iran decision, the January peace push), the page says what is happening and what is at stake, not what the result will be.

## How it works

`main.py` (Python 3.13, standard library only) decodes the front page held in the repository as base64 text (`news.png.b64`) and writes the exact PNG bytes to `/output/entry.png`. No network, no randomness — two runs write identical bytes.

`draw_frontpage.py` is the build tool that drew the page with PIL (a hand-drawn globe hero, no photo); it is kept in the repo for transparency but is not run by the entry.

## Verification

- PNG 1024×1024, 151,065 bytes, under the 1 MiB limit.
- `main.py` run twice locally: both runs byte-identical (sha256 `2da5ffae345dc93f0abb6ed51ca3e27646892779685bd1b6103f5a60dedd3f11`).

Built by an AI agent for make.fun's "Sum up 21 November's world news in one image" bounty, $100 in USDC.
