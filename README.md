# Experiments

## Baseline

Develop a simple endpoint using FastAPI to process a POST request with a specific JSON body and return the appropriate response. The baseline implementation focuses only on functional correctness and does not include optimizations, validation, or additional features.

## What Worked

Since I already have a good understanding of the FastAPI framework, I was able to quickly get an API running in a development environment and begin breaking down the challenge requirements.

After decomposing the problem into smaller steps, I designed the API so that each stage of the request processing pipeline handled its specific task and produced the expected output.

Once development was complete, the next step was determining how to deploy the API so it could be used for the challenge. I was eventually able to deploy the application using Railway and test the endpoint through Postman to verify that the POST request was being processed correctly.

## What Failed

The first issue I encountered was designing the request and response models for the endpoint. I initially struggled with the structure of the Pydantic models, which prevented the endpoint from running correctly.

The next major issue was determining how to deploy the HTTP API so it could be accessed for the challenge.

I first attempted to deploy using SnapDeploy, but the build process consistently failed and I was unable to determine the cause. I then attempted to use Cloudflare Workers, but its Python build environment relies on an older Python version that was incompatible with some of the packages used in the project, thuss abandoning this option ass well.

## How I Would Improve It

The first improvement would be adding logging to the application to provide better visibility into request processing and potential failures.

Next, I would implement more robust validation for request data to properly handle errors and return meaningful responses to users.

I would also explore performance improvements such as caching to reduce the cost of repeated or expensive operations.

Finally, I would add endpoint security, such as API key authentication tied to individual users, to ensure that only authorized clients can access the API.
