from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,   
    DateTime,
)

from datetime import datetime, timezone
from db.base import Base

class GithubEvent(Base):
    __tablename__ = "github_events"
    id = Column(Integer, primary_key=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    delivery_id = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))