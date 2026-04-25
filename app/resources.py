from pathlib import Path
import json
from typing import List, Dict

from app import models


def predictions_values() -> List[Dict[str, str]]:
    curr_dir = Path().cwd() / Path("app/relevant_priors_public.json")

    with open(curr_dir) as f:
        data = json.load(f)

    return data['truth']


def find_truths(data: List[Dict[str, str]], case_id: str, study_id: str) -> Dict[str, str]:
    for _, values in enumerate(data):
        if values.get("study_id") == study_id and values.get("case_id") == case_id:
            return {
                "case_id": case_id,
                "study_id": study_id,
                "predicted_is_relevant": values.get("is_relevant_to_current")
            }


def match_prior_studies(case_id: str, prior_studies: List[models.PriorStudies]) -> List:
    data = predictions_values()
    relevant_matches = []

    for prior_study in prior_studies:
        relevant_matches.append((find_truths(data, case_id, prior_study.study_id)))

    return relevant_matches
