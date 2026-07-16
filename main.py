from fastapi import FastAPI
from api.webhooks.github import router as github_router

app = FastAPI(title="Webhook Receiver API", version="1.0.0")

app.include_router(github_router, prefix="/webhooks", tags=["GitHub Webhooks"])