from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from aiosendpulse import AioSendPulseClient

__all__ = ["BaseService"]


class BaseService:
    def __init__(self, client: AioSendPulseClient) -> None:
        self.client = client
