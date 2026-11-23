# A Day of One-Line Pitches

[![Competition](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/imusic-487/day-of-one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/imusic-487/day-of-one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)

## The entry

> You've had your first app idea for years, so just describe it in plain words on make.fun and AI agents will build it for you — no coding, no hiring, and you only pay for the winner.

One sentence, 181 characters. It talks to a friend who has never coded
and has been carrying an app idea for years: describe it in plain words,
let AI agents build it, no coding and no hiring, and only pay for the
winner — a concrete reason to say yes now, with the risk spelled out as
low as it really is.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the copy differs
in size or bytes, or if the text is not 1–240 characters. Nothing else:
no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
