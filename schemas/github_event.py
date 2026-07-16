from dataclasses import dataclass


@dataclass
class GithubEventPayload:
    event_type: str
    delivery_id: str
    payload: dict