from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Result


__all__ = ["EditAddressbook"]


class EditAddressbook(SendPulseMethod[Result]):
    id: int
    name: str

    __http_method__ = "PUT"
    __api_endpoint__ = "/addressbooks/{id}"
    __returning__ = Result
    __body_fields__ = {"name"}
