print("LOADED:", __file__)
from fastapi import (APIRouter, Request, Header, HTTPException, BackgroundTasks)

from security.github_signature import verify_github_signature
from services.github_event_service import save_event
from schemas.github_event import GithubEventPayload

router = APIRouter()

@router.post("/github")
async def github_webhook(
    request: Request,
    background_tasks: BackgroundTasks):

    body = await request.body()

    signature = request.headers.get('X-Hub-Signature-256')

    if not signature:
        raise HTTPException(
            status_code=400, detail="Missing X-Hub-Signature-256 header"
        )
    if not verify_github_signature(body, signature):
        raise HTTPException(
            status_code=400, detail="Invalid signature"
        )
    
    payload = await request.json()
    event_type = request.headers.get('X-GitHub-Event')
    delivery_id = request.headers.get('X-GitHub-Delivery')

    github_event = GithubEventPayload(
        event_type=event_type,
        delivery_id=delivery_id,
        payload=payload
    )

    background_tasks.add_task(save_event, github_event)
    return {
        "status": "success"}