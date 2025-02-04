from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import TotalEmails


__all__ = ["GetTotalEmails"]


class GetTotalEmails(SendPulseMethod[TotalEmails]):
    id: int

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks/{id}/emails/total"
