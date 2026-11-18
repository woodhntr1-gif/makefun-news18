# makefun-news18

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/woodhntr1-gif/makefun-news18/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/woodhntr1-gif/makefun-news18/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper front page summing up **Wednesday 18 November 2026** in one
image — drawn entirely with PIL (real text, flat vector illustration, no
AI-generated imagery, no photos).

## The image

`entry.png` (1024×1024, ~134 KB) is "THE WORLD IN ONE IMAGE", dated
**WEDNESDAY · 18 NOVEMBER 2026**. Lead story: the Kerch Bridge's road deck
falling into the sea after Ukraine's second strike in two days, with a drawn
illustration of the damaged bridge. Six further stories across regions and
fields — Trump in Manila ahead of the Xi meeting, Nvidia's doubled revenue
and the Dow's 849-point fall, the Bahrain drone attacks and the U.S. reply,
Britain's sanctions on settlement firms, Cyclone Akvan bearing down on
India, and India's 10th SAFF title — plus an "ALSO TODAY" strip (Canada–
China trade, UN civilian casualty figures, Modi's e-visa proposal and
Amazon's $7bn India renewables pledge).

## Sources (all reported headlines; claims are attributed in the image)

- Kerch Bridge collapse / Kyiv bridges: Reuters, BBC Verify, NBC News
  (via EuropeSays, Internewscast, Nexus Europa, 17–18 Nov 2026)
- Trump in Manila / ASEAN summit: The Philippine Star via AFP, AP
  (MoneyClub Daily Scan, 18 Nov 2026)
- Nvidia $115.8bn revenue (+103%), Dow −849: The Motley Fool, Morningstar,
  i3investor Daily Brief (17–18 Nov 2026)
- Bahrain / Sheikh Isa drones, U.S. strike on Qeshm Island: Al Jazeera,
  Reuters, U.S. Central Command, CBS News (17 Nov 2026)
- UK sanctions on eight settlement firms: Reuters (17 Nov 2026)
- Cyclone Akvan, landfall forecast 20 Nov: India Meteorological Department
  (via CareerIndia, Telangana Tribune, 16–17 Nov 2026)
- India 2–1 Pakistan, 10th SAFF title: IANS, AIFF (17 Nov 2026)
- Canada–China trade, UN figures, Modi e-visas, Amazon $7bn: as briefed
  from Jagran Josh / Education Times / AppiSToS round-ups of 17 Nov 2026

## Honesty note

The image was built on 18 Nov 2026 at ~02:10 UTC, while the day was still
in progress, so it covers the news as reported up to that point — mostly
stories that broke on Tuesday 17 Nov and overnight into Wednesday 18 Nov,
which is what a Wednesday paper carries. No event, number, or quote was
invented; where a figure was uncertain it is phrased as reported
("Iran said…", "Bahrain said…", "officials said…"). **A refresh on
19 Nov is advisable** before the 20 Nov deadline if bigger 18-Nov stories
break later in the day — re-run `draw.py` with an updated story list.

## Run it

```sh
python3 draw.py            # regenerate entry.png (needs Pillow + DejaVu fonts)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies entry.png to out/entry.png
```

`main.py` is Python 3.13 standard library only: it copies `entry.png` beside
it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It
makes no network calls and its output is byte-identical on every run.

## Files

| Path | What |
| --- | --- |
| `main.py` | Entry program (stdlib only). Copies `entry.png` to the output dir. |
| `entry.png` | The entry image, 1024×1024 PNG, ≤1 MiB. |
| `draw.py` | The PIL generator that renders `entry.png` from the story list. |
| `README.md` | This file. |
| `LICENSE` | MIT. |

---

<sub>Entered on [make.fun](https://make.fun/?ref=rez34v58&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>

---

# The World in One Image — make.fun bounty `news-image-20261118`

- Bounty: https://make.fun/bounty/news-image-20261118 — $250 (50 places paid)
- Deadline: 20 Nov 2026 00:00 UTC (07:00 WIB)
- Status: **built and tested locally only — NOT submitted** (no sign-in, no payment, no account/wallet created)

## Remaining for submission (not done, per instructions)

Public GitHub repo created after the bounty opened (18 Nov 2026) holding this
folder, entry signed by the user's Solana wallet on their make.fun account —
before 20 Nov 2026 00:00 UTC. Consider refreshing the image on 19 Nov with
the full day's news first (see honesty note above).
