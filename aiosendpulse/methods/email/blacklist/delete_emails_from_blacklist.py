from base64 import b64encode
from typing import Annotated

from pydantic import EmailStr, PlainSerializer

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Result


class DeleteEmailsFromBlacklist(SendPulseMethod[Result]):
    emails: Annotated[
        list[EmailStr], PlainSerializer(func=lambda x: b64encode(",".join(x).encode()).decode(), return_type=str)
    ]

    __http_method__ = "DELETE"
    __api_endpoint__ = "/blacklist"
    __returning__ = Result
    __body_fields__ = {"emails"}
