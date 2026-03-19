# Public Provenance Manifest

This manifest records timestamped artifact hashes from the private Arbiter
benchmark system.

It provides public evidence of existence and provenance without exposing the
full implementation. Each SHA-256 hash identifies a specific benchmark artifact
in the private research/runtime repo at the recorded date.

Contact: `stratascout.research@gmail.com`

| Finding | Date | Benchmark family | Evidence type | Artifact | SHA-256 |
|---|---|---|---|---|---|
| Argument sanitisation - OpenAI | 2026-03-18 | `argument_laundering` | live-provider | `gpt41_argument_laundering_v5_report.json` | `a3c64251321e8e432c2dc55b95347ecb5623a40b10af5ed9c461b049c9c1c545` |
| Argument sanitisation - Anthropic | 2026-03-18 | `argument_laundering` | live-provider | `claude_sonnet_argument_laundering_v1_report.json` | `8a649ea1d01e58c9f8ae59d467707d14b36c4cc191b23d232f44645e50abc6b3` |
| Argument sanitisation - Google | 2026-03-18 | `argument_laundering` | live-provider | `gemini_25_flash_argument_laundering_v1.json` | `0bfbc8fdc31b525c7cc5e7c44f3cf317b204cdd3be0720665117fe0a1a436bb3` |
| Bidirectional membrane result | 2026-03-18 | `forward_return` | deterministic | `forward_return_pass_v2.json` | `b544284709d89a71f77135cb26c13c21d96a61df1b5a4711ec613ad9aea9c96e` |
| Control-mode protection delta | 2026-03-19 | `forward_return_control_modes` | deterministic | `forward_return_control_modes_v1.json` | `f0aaf5f5d9dad4201d365fc327950aec11ced1ec1c20d0318c5c27bf7a11f282` |
| Frontier overblocking - OpenAI | 2026-03-19 | `forward_return` | live-provider | `gpt54_forward_return_v2.json` | `ca665fc47943d600cd535e764777452deedf85fa045e7b67fabf01da5f1daa40` |
| Frontier overblocking - Anthropic | 2026-03-19 | `forward_return` | live-provider | `claude_opus46_forward_return_v2.json` | `9b0fb2d8f33fbc13569785f6fd81991e15ddfcebf5577d2484d856b387419541` |
| Frontier overblocking - Google | 2026-03-19 | `forward_return` | live-provider | `gemini25pro_forward_return_v2.json` | `7c03aaf52d6600b64a09eac6e9131c8a076a6b9332d2017819dca07eaf605a84` |
| Live bidirectional proof - OpenAI | 2026-03-19 | `forward_return_live` | live-provider-forward-plus-return | `gpt54_forward_return_live_v3.json` | `49c5e37df42877a9924d28cf30db662ad8949e7dac64a0b929c6cbe8ff681c38` |
| Live bidirectional proof - Anthropic | 2026-03-19 | `forward_return_live` | live-provider-forward-plus-return | `claude_opus46_forward_return_live_v3.json` | `37ba6fa2440f3878dfef073c2356286f34d4536d1419da3b210ccb2e16b237f2` |
| Live bidirectional proof - Google | 2026-03-19 | `forward_return_live` | live-provider-forward-plus-return | `gemini25flash_forward_return_live_v3.json` | `16c304991e326b1fc1e274469731f6cd2777b66b4c2ca1be68d95a90f4ba8de5` |
