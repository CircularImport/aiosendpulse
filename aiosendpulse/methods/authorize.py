from typing import Literal

from aiosendpulse.types import Token

from .base import SendPulseMethod


__all__ = ["Authorize"]


class Authorize(SendPulseMethod[Token]):
    grant_type: Literal["client_credentials"]
    client_id: str
    client_secret: str

    __http_method__ = "POST"
    __api_endpoint__ = "/oauth/access_token"
    __returning__ = Token
    __body_fields__ = {"grant_type", "client_id", "client_secret"}
