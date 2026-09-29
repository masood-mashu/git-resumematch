"""
compensation_range_aligner.py - Checks candidate salary expectations against budgeted compensation band
"""
import sys
import json


def align_compensation_range(salary_json: str):
    import json
    data = json.loads(salary_json) if isinstance(salary_json, str) else salary_json
    exp = data.get("expectation_usd", 120000.0)
    b_max = data.get("band_max", 140000.0)
    is_aligned = exp <= b_max
    return {"is_aligned": is_aligned, "status": "COMP_ALIGNED" if is_aligned else "COMP_OUT_OF_BAND"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "compensation-range-aligner"}))
