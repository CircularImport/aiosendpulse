from base64 import b64encode
from typing import Annotated, Union

from pydantic import PlainSerializer
from pydantic_extra_types.language_code import LanguageAlpha2

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import CreateTemplateResult


__all__ = ["CreateTemplate"]


class CreateTemplate(SendPulseMethod[CreateTemplateResult]):
    name: Union[str, None] = None
    body: Annotated[
        str, PlainSerializer(func=lambda x: b64encode(x.encode()).decode(encoding="utf-8"), return_type=str)
    ]
    lang: LanguageAlpha2

    __http_method__ = "POST"
    __api_endpoint__ = "/template"
    __returning__ = CreateTemplateResult
    __body_fields__ = {"name", "body", "lang"}
