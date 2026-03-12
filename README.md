# Arbiter Public

Public-facing repository for Arbiter, a judgement layer for AI and operator workflows.

Arbiter is a judgement layer that sits between noisy candidate generation and downstream action. It takes a candidate payload, evaluates the available evidence, and returns a structured judgement such as `promoted`, `watchlist`, or `rejected`.

This repository is a minimal public demonstration of the judgement contract. It is not the full internal Arbiter engine or validation stack.

## Current status

The public repo currently exposes a small, deterministic demo of the input/output contract. It is intended to show the shape of the system clearly and honestly, not to publish the private kernel or full validation machinery.

## What is in this repo

- JSON schemas for a minimal request and response contract
- example request and response payloads
- a small deterministic demo runner

## What is not in this repo

- the full internal kernel
- private scoring logic
- internal validation harnesses
- deployment or production infrastructure

## Demo

Run the demo from the repository root:

```bash
python demo/run.py
```

It reads [`examples/sample_request.json`](./examples/sample_request.json) and prints a structured judgement response.

Example output:

```json
{
  "candidate_id": "case_001",
  "judgement": "promoted",
  "confidence": 0.81,
  "reason_summary": "Strong fit, recent supporting evidence, and acceptable evidence depth justify immediate review.",
  "key_factors": [
    "High relevance to target profile",
    "Evidence is recent",
    "Multiple sources support the candidate"
  ],
  "recommended_action": "prioritise_for_review"
}
```

## Repo structure

- [`schemas/arbiter_request.schema.json`](./schemas/arbiter_request.schema.json)
- [`schemas/arbiter_response.schema.json`](./schemas/arbiter_response.schema.json)
- [`examples/sample_request.json`](./examples/sample_request.json)
- [`examples/sample_response_promoted.json`](./examples/sample_response_promoted.json)
- [`examples/sample_response_watchlist.json`](./examples/sample_response_watchlist.json)
- [`examples/sample_response_rejected.json`](./examples/sample_response_rejected.json)
- [`demo/run.py`](./demo/run.py)

## Positioning

Arbiter is best understood as a judgement layer between candidate-generation systems and real downstream action. The current public demo focuses on a simple procurement-style example because that is the clearest narrow wedge.
