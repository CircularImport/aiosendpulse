from base64 import b64encode
from typing import Annotated, Union

from pydantic import PlainSerializer

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Result


__all__ = ["EditTemplate"]


class EditTemplate(SendPulseMethod[Result]):
    id: Union[str, int]
    body: Annotated[
        str, PlainSerializer(func=lambda x: b64encode(x.encode()).decode(encoding="utf-8"), return_type=str)
    ]

    __http_method__ = "POST"
    __api_endpoint__ = "/template/edit/{id}"
    __returning__ = Result
    __body_fields__ = {"body"}
