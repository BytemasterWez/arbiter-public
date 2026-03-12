# Arbiter public demo
# This is a minimal deterministic demonstration of the Arbiter judgement contract.
# It is not the full internal engine. See README for context.

import json
from pathlib import Path


def adjudicate(candidate: dict) -> dict:
    evidence = candidate.get("evidence", {})
    fit_score = evidence.get("fit_score", 0.0)
    freshness_days = evidence.get("freshness_days", 999)
    source_count = evidence.get("source_count", 0)

    if fit_score >= 0.75 and freshness_days <= 7 and source_count >= 2:
        judgement = "promoted"
        confidence = 0.81
        reason_summary = (
            "Strong fit, recent supporting evidence, and acceptable evidence depth justify immediate review."
        )
        key_factors = [
            "High relevance to target profile",
            "Evidence is recent",
            "Multiple sources support the candidate",
        ]
        recommended_action = "prioritise_for_review"

    elif fit_score >= 0.5:
        judgement = "watchlist"
        confidence = 0.63
        reason_summary = (
            "Candidate shows some relevance but does not yet justify immediate action."
        )
        key_factors = [
            "Moderate fit to target profile",
            "Evidence is incomplete or weaker",
            "Worth monitoring or enriching",
        ]
        recommended_action = "hold_for_recheck"

    else:
        judgement = "rejected"
        confidence = 0.78
        reason_summary = (
            "Current evidence does not support prioritising this candidate."
        )
        key_factors = [
            "Low fit to target profile",
            "Insufficient evidence strength",
            "Action would not be justified at this stage",
        ]
        recommended_action = "suppress"

    return {
        "candidate_id": candidate.get("candidate_id", "unknown"),
        "judgement": judgement,
        "confidence": confidence,
        "reason_summary": reason_summary,
        "key_factors": key_factors,
        "recommended_action": recommended_action,
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    sample_path = root / "examples" / "sample_request.json"

    with sample_path.open("r", encoding="utf-8") as file_handle:
        candidate = json.load(file_handle)

    result = adjudicate(candidate)

    print("Arbiter demo result:\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
