from dataclasses import dataclass


@dataclass
class GithubEvent:
    event_type: str
    delivery_id: str
    payload: dict