from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Generic, Literal, TypeVar, Union, get_args, get_origin

from httpx import URL, Request
from pydantic import BaseModel

from aiosendpulse.types.base import SendPulseObject


if TYPE_CHECKING:
    from aiosendpulse import AioSendPulseClient


__all__ = ["SendPulseMethod"]


SendPulseType = TypeVar("SendPulseType")


class SendPulseMethod(SendPulseObject, Generic[SendPulseType]):
    __http_method__: ClassVar[str]
    __api_endpoint__: ClassVar[str]
    __returning__: ClassVar[type]
    __query_fields__: ClassVar[set[str]] = set()
    __body_fields__: ClassVar[set[str]] = set()
    __content_type__: ClassVar[Literal["application/json"]] = "application/json"

    def build_request(self, base_url: URL) -> Request:
        params = {}
        body = {}
        for key, value in self.model_dump(mode="json", exclude_none=True, by_alias=True).items():
            if key in self.__query_fields__:
                params[key] = value

            if key in self.__body_fields__:
                body[key] = value

        return Request(
            method=self.__http_method__,
            url=base_url.join(url=self.__api_endpoint__.format_map(self)),
            params=params,
            json=body,
        )

    def __getitem__(self, item: str) -> Any:
        return getattr(self, item)

    async def __call__(self, client: AioSendPulseClient) -> Union[SendPulseType, dict, None]:
        response = await client.send(request=self.build_request(base_url=client.base_url))
        decoded_data = response.json()
        if get_origin(self.__returning__) is list:
            args = get_args(self.__returning__)
            if len(args) >= 1:
                raise ValueError()

            args = args[0]
            if issubclass(args, BaseModel):
                return [args.model_validate(obj=obj) for obj in decoded_data]

        if issubclass(self.__returning__, BaseModel):
            return self.__returning__.model_validate(obj=decoded_data)

        return decoded_data
