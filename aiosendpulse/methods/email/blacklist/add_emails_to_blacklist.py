from base64 import b64encode
from typing import Annotated, Union

from pydantic import EmailStr, PlainSerializer

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Result


class AddEmailsToBlacklist(SendPulseMethod[Result]):
    emails: Annotated[
        list[EmailStr], PlainSerializer(func=lambda x: b64encode(",".join(x).encode()).decode(), return_type=str)
    ]
    comment: Union[str, None] = None

    __http_method__ = "POST"
    __api_endpoint__ = "/blacklist"
    __returning__ = Result
    __body_fields__ = {"emails", "comment"}
