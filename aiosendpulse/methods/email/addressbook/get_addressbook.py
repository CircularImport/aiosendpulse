from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Addressbook


__all__ = ["GetAddressbook"]


class GetAddressbook(SendPulseMethod[list[Addressbook]]):
    id: int

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks/{id}"
    __returning__ = list[Addressbook]
