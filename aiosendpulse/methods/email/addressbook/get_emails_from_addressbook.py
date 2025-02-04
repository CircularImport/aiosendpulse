from typing import Union

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import EmailDetail


__all__ = ["GetEmailsFromAddressbook"]


class GetEmailsFromAddressbook(SendPulseMethod[list[EmailDetail]]):
    id: int
    limit: Union[int, None] = None
    offset: Union[int, None] = None
    active: Union[bool, None] = None
    not_active: Union[bool, None] = None

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks/{id}/emails"
    __returning__ = list[EmailDetail]
    __query_fields__ = {"limit", "offset", "active", "not_active"}
