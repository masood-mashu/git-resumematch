# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitResumeMatch** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitResumeMatch Automation Engine`
* **Responsibilities**:
  * Parses candidate experience, aligns skills with job requisition rubrics, and strips demographic markers.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitResumeMatch Verification & Policy Enforcer`
* **Responsibilities**:
  * Audits scoring distributions to ensure compliance with EEOC non-discrimination guidelines.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Head of Talent Acquisition / Hiring Manager (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
