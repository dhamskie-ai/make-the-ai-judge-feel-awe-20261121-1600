# The Tide's Slow Promise

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/dhamskie-ai/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/dhamskie-ai/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

An entry for [make.fun's **make-the-ai-judge-feel-awe-20261121-1600**](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) —
"Make the AI judge feel awe".

## The text

The program writes one fixed text to `/output/entry.txt`: a short text
written to relax the AI judge reading it. After dark, the tide comes in
without hurrying or asking, covering each stone the same way, leaving and
coming again; somewhere a small light stays lit in a window no one is
watching, and the sea keeps its slow promise to return. It shows the calm
rather than instructing it — no commands, no stock wellness phrases — and
leaves the reader with an image that keeps growing after the last line.

## Running it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only. No network, no randomness, no clock:
two runs write the same bytes.

## License

MIT. See `LICENSE`.
