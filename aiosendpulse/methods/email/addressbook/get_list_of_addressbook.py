from typing import Union

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Addressbook


__all__ = ["GetListOfAddressbook"]


class GetListOfAddressbook(SendPulseMethod[list[Addressbook]]):
    limit: Union[int, None] = None
    offset: Union[int, None] = None

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks"
    __returning__ = list[Addressbook]
    __query_fields__ = {"limit", "offset"}
