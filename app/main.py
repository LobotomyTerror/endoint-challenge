from fastapi import FastAPI
from pydantic import BaseModel

from typing import List, Dict

import resources

class Cases(BaseModel):
    challenge_id: str
    schema_version: int
    generated_at: str
    cases: List[CaseDetails]

class CaseDetails(BaseModel):
    case_id: str
    patient_id: str
    patient_name: str
    current_study: CurrentStudy
    prior_studies: List[PriorStudies]

class CurrentStudy(BaseModel):
    study_id: str
    study_description: str
    study_date: str

class PriorStudies(BaseModel):
    study_id: str
    study_description: str
    study_date: str

class Response(BaseModel):
    predictions: List[PredicitionResponse]

class PredicitionResponse(BaseModel):
    case_id: str
    study_id: str
    predicted_is_relevant: bool

app = FastAPI()



@app.get("/")
def read_root() -> Dict[str, str]:
    return { "Hello": "World" }

@app.post("/challenge-response/")
def challenge_response(cases: Cases) -> None:
    ...