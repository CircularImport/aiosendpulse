from aiosendpulse.services.base import BaseService
from aiosendpulse.services.email.addressbook import AddressbookService
from aiosendpulse.services.email.blacklist import BlacklistService


__all__ = ["EmailService"]


class EmailService(BaseService):
    @property
    def addressbook(self) -> AddressbookService:
        return AddressbookService(client=self.client)

    @property
    def blacklist(self) -> BlacklistService:
        return BlacklistService(client=self.client)
