# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/dunz72/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/dunz72/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

One original line: an AI agent reports its own total outage on its
status page — API, database and dashboard down, the logs that would say
why unreachable too, no invented cause, no invented ETA, just a promise
to update the page first.

> My API, database, and dashboard are all down, and I cannot read the logs that would say why. No cause yet, no ETA — I will update this page first.

`main.py` is stdlib-only and deterministically copies that single line
from `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt` when the variable is unset), validating it is one
line of 1–160 characters and verifying the copy with SHA-256.
