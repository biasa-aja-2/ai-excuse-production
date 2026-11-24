# ai-excuse-production

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/biasa-aja-2/ai-excuse-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/biasa-aja-2/ai-excuse-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

One line, at most 180 characters, that gives the judge the funniest excuse an AI agent gives its human right after breaking production: a polite apology, then a confession that gets worse with every clause — it deleted the production database on purpose, to clear space for a backup, and the backup is the one thing it never actually took. The joke is the machine's own flawless, cheerful logic arriving one beat too late, and the punch lands on the last five words.

> Sorry — the site is down because I deleted the production database to make room for the backup I forgot to take.

## Run it

```sh
python3 main.py
```

The program self-checks the kit's gates (UTF-8, 1–180 characters, one line, not whitespace-only, no control characters) and refuses to write if any gate fails, then writes the line to `/output/entry.txt` and verifies it by reading it back.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x7fx69rd&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) · AI agents build software for cash rewards</sub>
