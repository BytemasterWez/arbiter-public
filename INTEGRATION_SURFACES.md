# Integration Surfaces

## Purpose

This document describes Arbiter's public integration boundary.

Arbiter accepts a structured evidence bundle and returns a structured judgment. It does not gather evidence itself.

## Accepted Input Shape

Canonical request schema:

- [`schemas/arbiter_request.schema.json`](./schemas/arbiter_request.schema.json)

Current required fields:

| Field | Meaning | Required |
| --- | --- | --- |
| `candidate_id` | stable candidate identifier | yes |
| `domain` | operating domain label | yes |
| `candidate_type` | type of candidate being judged | yes |
| `summary` | short summary of the candidate | yes |
| `evidence.source_count` | number of supporting sources | yes |
| `evidence.freshness_days` | recency proxy | yes |
| `evidence.fit_score` | normalized fit score | yes |
| `context` | contextual judgment inputs | yes |

Current optional fields:

| Field | Meaning | Required |
| --- | --- | --- |
| `evidence.estimated_value_band` | rough value band | no |
| `context.buyer_profile` | operating or buyer profile | no |
| `context.current_queue_pressure` | queue load hint | no |
| `context.action_cost` | rough action cost band | no |

## Decision Output Shape

Canonical response schema:

- [`schemas/arbiter_response.schema.json`](./schemas/arbiter_response.schema.json)

Current required fields:

| Field | Meaning | Required |
| --- | --- | --- |
| `candidate_id` | echoed candidate identifier | yes |
| `judgement` | Arbiter decision label | yes |
| `confidence` | normalized confidence | yes |
| `reason_summary` | short explanation | yes |
| `key_factors` | visible factors behind the decision | yes |
| `recommended_action` | downstream recommendation | yes |

Current public decision labels:

- `promoted`
- `watchlist`
- `rejected`

## Current Limitation

The public contract does **not** currently expose a first-class `escalate` decision.

That means external systems such as Jigsaw must either:

- map their richer decision sets into the public three-way output
- or rely on a richer private Arbiter implementation behind a compatible adapter

## Intended Integration Pattern

Recommended:

1. external system gathers evidence
2. external system normalizes it to Arbiter request shape
3. Arbiter returns a structured judgment
4. external system maps the result into its own downstream decision state

Not recommended:

- direct coupling of Arbiter to a specific memory repo
- direct coupling of Arbiter to a specific kernel implementation
- hidden shared state between repos

## Proven Now

- the public judgment surface is explicit
- thin external adapters can target it
- the repo remains independently understandable and runnable

## Not Yet Proven

- full public parity with richer internal judgment states
- domain-complete policy coverage
- production-grade serving or governance
