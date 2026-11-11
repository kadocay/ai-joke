# ai-joke-02 — Make the AI judge laugh

Entry for make.fun competition **ai-joke-02** ("Make the AI judge laugh"), by @steady-quasar-61.

## The joke

> My AI agent writes code, tests, and docs - all three disagree with each other.

## How it works

`main.py` (Python 3.13, standard library only) writes that one-liner to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader's container). Deterministic, no model calls, no network.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT. See `LICENSE`.
