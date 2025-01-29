from __future__ import annotations

from typing import Literal, Union

from httpx import AsyncClient

from aiosendpulse.auth import BearerTokenAuth
from aiosendpulse.methods import (
    Authorize,
)
from aiosendpulse.methods.email.blacklist import AddEmailsToBlacklist, DeleteEmailsFromBlacklist
from aiosendpulse.methods.email.mailing import AddEmailsToMailingList
from aiosendpulse.methods.email.templates import CreateTemplate, EditTemplate, GetTemplate
from aiosendpulse.types import CreateTemplateResult, EmailDetail, Result, Template


__all__ = ["AioSendPulseClient"]


BASE_URL: str = "https://api.sendpulse.com"


class AioSendPulseClient:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        grant_type: Literal["client_credentials"] = "client_credentials",
        token: str = None,
    ) -> None:
        self.client = AsyncClient(base_url=BASE_URL)
        self.auth_class: type[BearerTokenAuth] = BearerTokenAuth
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__grant_type = grant_type
        self.__auth: Union[BearerTokenAuth, None] = None

        if token is not None:
            self.__auth = self.auth_class(token=token)

    @property
    def token(self) -> Union[str, None]:
        if self.__auth is not None:
            return self.__auth.token

    async def __aenter__(self) -> AioSendPulseClient:
        if not self.__auth:
            await self.authorize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self) -> None:
        await self.client.aclose()

    async def authorize(self) -> None:
        method = Authorize(
            client_id=self.__client_id,
            client_secret=self.__client_secret,
            grant_type=self.__grant_type,
        )
        response = await method(client=self.client)
        self.__auth = self.auth_class(
            token=response.access_token.get_secret_value(),
        )

    # Email service / mailing section
    async def add_emails_to_mailing_list(self, mailing_list_id: int, emails: list[Union[EmailDetail, dict]]) -> Result:
        return await AddEmailsToMailingList(
            mailing_list_id=mailing_list_id,
            emails=emails,
        )(client=self.client, auth=self.__auth)

    # Email service /blacklist section
    async def add_emails_to_blacklist(self, emails: list[str], comment: str = None) -> Result:
        return await AddEmailsToBlacklist(
            emails=emails,
            comment=comment,
        )(client=self.client, auth=self.__auth)

    async def delete_emails_from_blacklist(self, emails: list[str]) -> Result:
        return await DeleteEmailsFromBlacklist(emails=emails)(client=self.client, auth=self.__auth)

    # Email service / templates section
    async def create_template(self, html: str, lang: str, name: str = None) -> CreateTemplateResult:
        return await CreateTemplate(
            name=name,
            body=html,
            lang=lang,  # noqa
        )(client=self.client, auth=self.__auth)

    async def edit_template(self, template_id: Union[str, int], html: str) -> Result:
        return await EditTemplate(
            id=template_id,
            body=html,
        )(client=self.client, auth=self.__auth)

    async def get_template(self, template_id: Union[str, int]) -> Template:
        return await GetTemplate(
            template_id=template_id,
        )(client=self.client, auth=self.__auth)
