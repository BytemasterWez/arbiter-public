# Public Scope and Repo Map

This repository is the public evidence and minimal-contract surface for
Arbiter.

It is intentionally narrower than the full current private system.

The goal of this repo is to let outside readers verify that:

- Arbiter is a real project rather than a vague idea
- the main findings have been written down publicly
- live bidirectional proof artifacts exist and are publicly recorded by hash
- a minimal public judgment contract can be demonstrated in a standalone repo

It is not intended to expose the full private runtime, benchmark harness, or
current orchestration/control-plane work.

## What this repo contains

### 1. Public evidence

The strongest public evidence surface is:

- [FINDINGS.md](./FINDINGS.md)
- [LIVE_BIDIRECTIONAL_PROOF.md](./LIVE_BIDIRECTIONAL_PROOF.md)
- [PUBLIC_PROVENANCE_MANIFEST.md](./PUBLIC_PROVENANCE_MANIFEST.md)

These documents are the public record of what Arbiter has found so far and
which private artifacts those findings correspond to.

### 2. Minimal public contract demo

This repo also contains a small deterministic demo surface:

- [schemas/arbiter_request.schema.json](./schemas/arbiter_request.schema.json)
- [schemas/arbiter_response.schema.json](./schemas/arbiter_response.schema.json)
- [INTEGRATION_SURFACES.md](./INTEGRATION_SURFACES.md)
- [demo/run.py](./demo/run.py)

These files should be read as a minimal public contract demo.

They are useful because they show:

- how a structured request/response boundary can look
- the promoted/watchlist/rejected decision shape
- the idea of separating evidence preparation from judgment

They should not be read as the complete current Arbiter protocol.

### 3. Narrow integration example

The integration materials in this repo show one simple way to target Arbiter
from an outside system.

They do not expose:

- the full private forward-pass contract
- the private reverse-pass verification runtime
- the full benchmark stack
- the bridge/control-plane architecture

## What remains private

The broader private Arbiter system currently includes work that is not
published here, including:

- the richer forward-pass request/response contract used in the current
  private runtime
- the reverse-pass verification runtime
- comparative control-mode benchmarking
- cross-provider live benchmarking harnesses
- bridge-server and orchestration design work
- adaptive-layer exploratory research
- broader artifact and telemetry handling

That split is intentional.

## How to read this repo correctly

If you want:

- the public findings and proof surface:
  start with [FINDINGS.md](./FINDINGS.md) and
  [LIVE_BIDIRECTIONAL_PROOF.md](./LIVE_BIDIRECTIONAL_PROOF.md)

- the public receipts:
  read [PUBLIC_PROVENANCE_MANIFEST.md](./PUBLIC_PROVENANCE_MANIFEST.md)

- the minimal public contract demo:
  read [INTEGRATION_SURFACES.md](./INTEGRATION_SURFACES.md) and the schemas

The most important thing to understand is this:

this repository is best read as a public evidence package plus a narrow demo
surface, not as a full public dump of the current private Arbiter system.
