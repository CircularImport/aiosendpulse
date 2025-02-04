from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import EmailDetail


__all__ = ["SearchEmails"]


class SearchEmails(SendPulseMethod[list[EmailDetail]]):
    id: int
    variable_name: str
    search_value: str

    __http_method__ = "GET"
    __api_endpoint__ = "/addressbooks/{id}/variables/{variable_name}/emails/{search_value}"
    __returning__ = list[EmailDetail]
