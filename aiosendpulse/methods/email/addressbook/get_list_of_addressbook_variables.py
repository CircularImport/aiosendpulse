from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import AddressbookVariable


__all__ = ["GetListOfAddressbookVariables"]


class GetListOfAddressbookVariables(SendPulseMethod[list[AddressbookVariable]]):
    id: int

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks/{id}/variables"
    __returning__ = list[AddressbookVariable]
