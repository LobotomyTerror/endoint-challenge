from fastapi import FastAPI
# from workers import WorkerEntrypoint
# import asgi

from typing import Dict

from app import resources, models

# class Default(WorkerEntrypoint):
#     async def fetch(self, request):
#         return await asgi.fetch(app, request, self.env)

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
