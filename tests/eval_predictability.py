"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitResumeMatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.skill_gap_analyzer import *
from tools.anonymized_profile_builder import *
from tools.compensation_range_aligner import *

class TestGitResumeMatchPredictability(unittest.TestCase):
    def test_skill_gap_analyzer(self):
        res = analyze_skill_gaps('{"candidate_skills": ["Python", "Docker", "SQL", "FastAPI"], "required_skills": ["Python", "SQL", "Docker"]}')
        self.assertEqual(res["match_pct"], 100.0)
        self.assertEqual(res["status"], "FIT_EXCELLENT")

    def test_anonymized_profile_builder(self):
        res = build_anonymized_profile("She graduated in 2004 with a degree in Computer Science.")
        self.assertIn("[CANDIDATE]", res["anonymized_profile"])
        self.assertEqual(res["status"], "PROFILE_ANONYMIZED")

    def test_compensation_range_aligner(self):
        res = align_compensation_range('{"expectation_usd": 130000.0, "band_max": 150000.0}')
        self.assertTrue(res["is_aligned"])
        self.assertEqual(res["status"], "COMP_ALIGNED")


if __name__ == "__main__":
    unittest.main()
