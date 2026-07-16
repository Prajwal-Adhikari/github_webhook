from fastapi import FastAPI
from api.webhooks.github import router as github_router
from contextlib import asynccontextmanager

from db.session import engine
from db.base import Base
from db.models.github_event import GithubEvent

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Drop the database tables (optional, for cleanup)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

app = FastAPI(title="Webhook Receiver API", version="1.0.0", lifespan=lifespan)

app.include_router(github_router, prefix="/webhooks", tags=["GitHub Webhooks"])

for route in app.routes:
    print(route)

for route in app.router.routes:
    if hasattr(route, "path"):
        print(route.path, route.methods)

print(github_router)
print(github_router.routes)