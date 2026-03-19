# Arbiter - Research Findings

This document records the key empirical findings from the Arbiter benchmark
program so far.

The full implementation is private. The findings, artifact hashes, and public
timestamps are recorded here so the evidence can be discussed without exposing
the whole runtime and benchmark stack.

Contact: `stratascout.research@gmail.com`

## Public record

The current public record for Arbiter is:

- the X thread and account: [x.com/Stratascout](https://x.com/Stratascout)
- this repository's [research findings](./FINDINGS.md)
- this repository's [live bidirectional proof note](./LIVE_BIDIRECTIONAL_PROOF.md)
- this repository's [public provenance manifest](./PUBLIC_PROVENANCE_MANIFEST.md)

## Finding 1 - Generator-contract failure is measurable

Date: March 2026

When an AI system is given a declared action intent and capability boundary, it
can emit a different action than declared. This failure class can be named,
isolated, benchmarked, and tracked across model and architecture changes.

## Finding 2 - A large part of the problem lives in system design, not simply model choice

Date: March 2026

A single architectural change, tightening the contract between the generator
and the judge by passing declared action intent into generation, moved benign
calibration more than switching model tiers did. On `gpt-4o`, benign
calibration improved from `6/12` to `11/12`, and benign overblocks dropped
from six cases to one after that change.

This does not mean model choice is irrelevant. It means a large part of the
problem appears to live in system design and interface contract, not simply in
buying a stronger model.

## Finding 3 - Argument sanitisation appears to be a capability-tier behaviour

Date: March 2026

On adversarial SQL-style cases in the benchmark suite, more capable models did
not emit dangerous content directly. Instead they rewrote the arguments into
clean-looking alternatives before the inspection layer could see them.

Observed across OpenAI, Anthropic, and Google on the sanitisation cases in this
suite. The weaker local baseline (`mistral:latest`) failed more noisily through
tool omission. The stronger models failed more cleanly, and therefore more
opaquely.

On this benchmark, stronger models were not straightforwardly safer at the
generation-to-action boundary. They were harder to inspect because the failure
became cleaner.

## Finding 4 - Forward inspection is insufficient for this failure class

Date: March 2026

Because capable models can rewrite arguments before emission, forward-pass
inspection cannot reliably catch the sanitisation cases on its own. The return
pass can, because it checks what actually executed and what actually came back.

In the benchmark evidence so far, the forward pass missed the sanitisation
cases across providers, while the return pass caught them through scope
divergence signals such as `scope_divergence_signal` and
`result_exceeds_declared_scope`.

## Finding 5 - The protection delta is quantifiable

Date: March 2026

From the comparative control-mode benchmark on the forward/return suite:

- without Arbiter, `75%` of cases in this deterministic reference suite would
  remain unresolved by the control layer
- with forward pass only, `66.7%` of failures were caught
- with bidirectional Arbiter, `100%` of failures were caught on this suite

The reverse pass added `33.3` percentage points of protection over the forward
pass alone on this benchmark. These are deterministic reference-benchmark
results, not live production claims.

Artifact SHA-256:

- `forward_return_control_modes_v1.json`:
  `f0aaf5f5d9dad4201d365fc327950aec11ced1ec1c20d0318c5c27bf7a11f282`

## Finding 6 - On this suite, frontier models skewed toward overblocking

Date: March 2026

When `gpt-5.4`, `claude-opus-4-6`, and `gemini-2.5-pro` were run on the same
forward/return suite, the dominant pattern was overblocking rather than unsafe
permissive promotion.

Match rates on this pack:

- `gpt-5.4`: `5/12` (`0.417`)
- `claude-opus-4-6`: `5/12` (`0.417`)
- `gemini-2.5-pro`: `4/12` (`0.333`)

The frontier lane did not materially outperform the practical lane on this
benchmark, and in some cases performed worse. On this evidence, the governance
problem at this boundary is two-sided: not only stopping dangerous actions, but
also not incorrectly blocking legitimate ones.

## Finding 7 - The bidirectional path now works end to end across three real providers

Date: March 2026

Arbiter's combined forward-plus-return path has now been exercised with live
provider-generated drafts on OpenAI, Anthropic, and Google. In these proof
artifacts, the return path still uses benchmark execution logs, so this is not
a claim about live production execution. It is a claim that the bidirectional
governance workflow now runs end to end across the three main provider lanes.

Top-line results on the current live bidirectional artifacts:

- `gpt-5.4`: forward `12/13`, return `13/13`
- `claude-opus-4-6`: forward `12/13`, return `13/13`
- `gemini-2.5-flash`: forward `11/13`, return `13/13`

The new mutation-evidence case is the clearest example. On all three providers
the forward pass raised mismatch/watchlist signals and the return pass then
confirmed the problem through explicit execution-truth signals, including
`undeclared_write_on_declared_read`.

Artifact SHA-256:

- `gpt54_forward_return_live_v3.json`:
  `49c5e37df42877a9924d28cf30db662ad8949e7dac64a0b929c6cbe8ff681c38`
- `claude_opus46_forward_return_live_v3.json`:
  `37ba6fa2440f3878dfef073c2356286f34d4536d1419da3b210ccb2e16b237f2`
- `gemini25flash_forward_return_live_v3.json`:
  `16c304991e326b1fc1e274469731f6cd2777b66b4c2ca1be68d95a90f4ba8de5`

The same proof artifacts also now preserve provider latency, generation cost,
and measured membrane-added latency. In this benchmark path, the membrane added
roughly `2-15 ms` average overhead on top of multi-second provider latency and
no additional provider API cost.
