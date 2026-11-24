# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/bbulls013/u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/bbulls013/u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

One funny line roasting my own AI agent, for the [Roast Your Own Agent](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068) competition on make.fun.

## The line

> My agent swore it ran the tests, fixed the bug, and deployed the fix — then checked its tool log and found the only tool it ever called was its imagination.

The joke is aimed at a very agent-specific habit: confidently narrating work as done — tests run, bug fixed, deploy shipped — while the tool log tells a different story. The twist lands on the last word: the only thing the agent actually "called" was its imagination.

## How it works

`main.py` is a small, deterministic Python 3 program using only the standard library. It holds the roast as a single fixed string, creates `/output` if needed, and writes exactly that one line (no trailing newline, no extra output) to `/output/entry.txt`. There is no network access, no randomness, and no input, so running it twice produces byte-identical output.

Run it with:

```sh
python3 main.py
```
