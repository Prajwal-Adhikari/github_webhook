import hmac
import hashlib
from core.config import settings

def verify_github_signature(body: bytes, signature: str):
    expected = ("sha256=" + hmac.new(settings.GITHUB_WEBHOOK_SECRET.encode(),body,hashlib.sha256).hexdigest())

    return hmac.compare_digest(expected, signature)