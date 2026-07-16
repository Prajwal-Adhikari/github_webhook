from sqlalchemy.exc import IntegrityError

from db.session import SessionLocal
from db.models.github_event import GithubEvent

async def save_event(event_type: str, delivery_id: str, payload: dict):
    async with SessionLocal() as session:
        event = GithubEvent(
            event_type=event_type,
            delivery_id=delivery_id,
            payload=payload
        )

        session.add(event)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
            print(f"Duplicate delivery_id: {delivery_id}. Event not saved.")