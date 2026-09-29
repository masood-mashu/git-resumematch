"""
anonymized_profile_builder.py - Removes personal demographic markers from resume text to prevent bias
"""
import sys
import json


def build_anonymized_profile(profile_text: str):
    import re
    cleaned = re.sub(r"\b(Mr\.|Ms\.|Mrs\.|He|She|His|Her)\b", "[CANDIDATE]", profile_text, flags=re.IGNORECASE)
    cleaned = re.sub(r"\b(19[5-9]\d|200\d)\b", "[GRAD_YEAR]", cleaned)
    return {"anonymized_profile": cleaned, "status": "PROFILE_ANONYMIZED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "anonymized-profile-builder"}))
