[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/amusu781/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/amusu781/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

# Worst Fix Ever: Funniest Commit Message

A program that writes one commit message — for a bug fix that made
everything worse — to `/output/entry.txt`.

## Entry

```
fix: evicted the bug from login, it moved into billing
```

54 characters. The fix chased the bug out of login; it relocated to
billing, where it now costs money.

## Running

```sh
python3 main.py
```

Standard library only, no network access. `main.py` creates `/output`
if needed, clears its contents (never the directory itself), and writes
the entry as UTF-8 text.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
