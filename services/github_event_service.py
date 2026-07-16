from sqlalchemy.exc import IntegrityError

from db.session import SessionLocal
from db.models.github_event import GithubEvent

async def save_event(event: GithubEvent):
    async with SessionLocal() as session:
        event = GithubEvent(
            event_type=event.event_type,
            delivery_id=event.delivery_id,
            payload=event.payload
        )

        session.add(event)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
            print(f"Duplicate delivery_id: {event.delivery_id}. Event not saved.")