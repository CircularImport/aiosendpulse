from typing import Annotated

from pydantic import Field

from aiosendpulse.methods.base import SendPulseMethod
from aiosendpulse.types import AddressbookId


__all__ = ["CreateAddressbook"]


class CreateAddressbook(SendPulseMethod[AddressbookId]):
    book_name: Annotated[str, Field(serialization_alias="bookName")]

    __http_method__ = "POST"
    __api_endpoint__ = "/addressbooks"
    __returning__ = AddressbookId
    __body_fields__ = "boolName"
