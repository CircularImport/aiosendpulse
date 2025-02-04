from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import EmailDetail, Result


__all__ = ["AddEmailsToAddressbook"]


class AddEmailsToAddressbook(SendPulseMethod[Result]):
    addressbook_id: int
    emails: list[EmailDetail]

    __http_method__ = "POST"
    __api_endpoint__ = "/addressbooks/{addressbook_id}/emails"
    __returning__ = Result
    __body_fields__ = {"addressbook_id", "emails"}
