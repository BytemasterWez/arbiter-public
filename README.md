# Arbiter Public

Arbiter is the judgment membrane in a larger three-repository architecture.

- Garbage Collector remembers.
- Jigsaw assembles explicit evidence.
- Arbiter judges whether action is permitted.

This repository is a public, minimal demonstration of the Arbiter contract. It is intentionally narrow and does not expose the full internal system.

## What Arbiter Is

Arbiter is a decision layer that accepts a structured evidence bundle and returns a structured judgment.

In this public repo, the exposed outputs are:

- `promoted`
- `watchlist`
- `rejected`

## What Arbiter Is Not

Arbiter is not:

- the memory substrate
- the evidence-gathering kernel chain
- the downstream action executor
- the full internal policy engine

## Role In The Larger Architecture

Arbiter sits between candidate preparation and action.

```text
Garbage Collector -> Jigsaw -> Arbiter -> Action
```

- Garbage Collector supplies recall and context
- Jigsaw converts candidates into explicit evidence bundles
- Arbiter decides whether action is justified

This repo remains independently usable as a standalone contract demo.

## Public Interfaces

- request schema: [`schemas/arbiter_request.schema.json`](./schemas/arbiter_request.schema.json)
- response schema: [`schemas/arbiter_response.schema.json`](./schemas/arbiter_response.schema.json)
- demo adjudicator: [`demo/run.py`](./demo/run.py)
- integration guide: [`INTEGRATION_SURFACES.md`](./INTEGRATION_SURFACES.md)

## Standalone Use

Run the deterministic demo from the repository root:

```bash
python demo/run.py
```

It reads [`examples/sample_request.json`](./examples/sample_request.json) and prints a structured response.

## Integration Use

Arbiter is designed to be called by an external capability layer such as Jigsaw.

The important rule is:

- integration should happen through the request/response contract
- not through hidden shared code
- not through a merged repo

## Proven Now

- a public request/response judgment contract exists
- the judgment surface is legible to outside readers
- the repo can stand alone as a deterministic contract demo
- Jigsaw can map into this public contract through a thin adapter

## Not Yet Proven

- the full private Arbiter policy stack
- first-class public `escalate` support
- production deployment, operations, or policy completeness
- broad domain coverage beyond the current narrow public wedge

## How This Fits Into The Larger Architecture

Arbiter is the layer that turns evidence into permission or refusal.

It should stay separate from:

- memory retrieval concerns
- kernelized evidence generation
- downstream action execution

That separation is the point of the architecture.
