from typing import Union

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import Template


__all__ = ["GetTemplate"]


class GetTemplate(SendPulseMethod[Template]):
    template_id: Union[int, str]

    __http_method__ = "GET"
    __api_endpoint__ = "/template/{template_id}"
    __returning__ = Template
