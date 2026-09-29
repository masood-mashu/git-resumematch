# Explainability, Auditability & Decision Logic: GitResumeMatch

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitResumeMatch**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitResumeMatch** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Candidate**: Candidate CV / Resume text and portfolio project summaries.
- **Corporate**: Corporate job requisition specifications and required competency matrices.
- **EEOC**: EEOC guidelines and organizational compensation benchmark bands.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **analyze_skill_gaps**: Uses `skill-gap-analyzer` to calculate computes overlap percentage between candidate competencies and job requirements.
   - **build_anonymized_profile**: Uses `anonymized-profile-builder` to calculate removes personal demographic markers from resume text to prevent bias.
   - **align_compensation_range**: Uses `compensation-range-aligner` to calculate checks candidate salary expectations against budgeted compensation band.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When a candidate profile is screened, the agent runs skill_gap_analyzer, anonymized_profile_builder, and compensation_range_aligner. If skills match >= 75% and comp is within band, it issues APPROVED. If skill match is 60–74%, it issues NEEDS_REVIEW. If missing mandatory core licensing or compensation exceeds maximum ceiling by > 30%, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on objective rubric matrices.
- **Does**: Does not conduct live interviews or record audio/visual candidate impressions.
- **Ensures**: Ensures complete anonymization of candidate identity until interview stage.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
