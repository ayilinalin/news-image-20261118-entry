# news-image-20261118 — entry

Newspaper front page summing up the world news of **Wednesday 18 November 2026**:

- **Trump lands in Manila** — Quad talks begin ahead of the China visit.
- **Crimea bridge hit again, day two** — Ukraine strikes the Kerch bridge for a second day running while Russia hits Kyiv bridges.
- **Iran drone strikes US radar in Bahrain** — the third drone attack on US assets in the region in days.
- **Nvidia revenue doubles** — first earnings since CEO Jensen Huang was fired; the board will not bring him back.

## How to run

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the bundled
`entry.png` (1024×1024, 266,507 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png`
with mode 0644. The program is deterministic: two runs write byte-identical
output.

## Competition

make.fun bounty `news-image-20261118` — one image summing up 18 November
2026's world news. License: MIT.
