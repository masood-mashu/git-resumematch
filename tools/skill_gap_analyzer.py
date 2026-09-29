"""
skill_gap_analyzer.py - Computes overlap percentage between candidate competencies and job requirements
"""
import sys
import json


def analyze_skill_gaps(skills_json: str):
    import json
    data = json.loads(skills_json) if isinstance(skills_json, str) else skills_json
    c_skills = [s.lower() for s in data.get("candidate_skills", [])]
    req_skills = [s.lower() for s in data.get("required_skills", [])]
    matched = [s for s in req_skills if s in c_skills]
    pct = round((len(matched) / max(len(req_skills), 1)) * 100, 1)
    status = "FIT_EXCELLENT" if pct >= 75.0 else ("FIT_MODERATE" if pct >= 60.0 else "SKILL_GAP")
    return {"match_pct": pct, "matched_skills": matched, "status": status}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "skill-gap-analyzer"}))
