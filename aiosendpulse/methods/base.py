from __future__ import annotations

from typing import ClassVar, Generic, TypeVar, Union

from httpx import URL, AsyncClient, Auth, HTTPError, HTTPStatusError, Request

from aiosendpulse.exceptions import ExceptionDispatcher
from aiosendpulse.logger import logger
from aiosendpulse.types.base import SendPulseObject


SendPulseType = TypeVar("SendPulseType", bound=SendPulseObject)


class SendPulseMethod(SendPulseObject, Generic[SendPulseType]):
    __http_method__: ClassVar[str]
    __api_endpoint__: ClassVar[str]
    __returning__: ClassVar[type]

    def build_request(self, base_url: URL) -> Request:
        raise NotImplementedError()

    async def __call__(self, client: AsyncClient, auth: Auth = None) -> Union[SendPulseType, dict, None]:
        request = self.build_request(base_url=client.base_url)
        try:
            response = await client.send(request, auth=auth)
        except HTTPError as e:
            logger.error(f"Calling method {self.__api_endpoint__} falling with exception: {e}")
        else:
            try:
                response.raise_for_status()
            except HTTPStatusError:
                data = response.json()
                exception = ExceptionDispatcher.get(error_code=data.get("error_code"), **self.model_dump())
                raise exception

            if issubclass(self.__returning__, SendPulseObject):
                return self.__returning__.model_validate_json(json_data=response.content)
            return response.json()
