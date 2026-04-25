from pathlib import Path
import json
from typing import Any, List


def predictions_values() -> Any:
    curr_dir = Path().cwd() / Path("app/relevant_priors_public.json")

    with open(curr_dir) as f:
        data = json.load(f)

    return data['truth']


def match_prior_studies(case_id: str, prior_studies: List) -> List:
    data = predictions_values()

    for i, values in enumerate(data):
        ...
