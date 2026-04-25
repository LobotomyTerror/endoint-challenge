from fastapi import FastAPI

from typing import Dict

from app import resources, models

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return { "Hello": "World" }


@app.post("/challenge-response/", response_model=models.Response)
def challenge_response(cases: models.Cases):
    results = []
    for case in cases.cases:
        results.extend(resources.match_prior_studies(case.case_id, case.prior_studies))

    return models.Response(predictions=results)
