from .addressbook import Addressbook, AddressbookId
from .addressbook_variable import AddressbookVariable
from .email import EmailDetail
from .result import CreateTemplateResult, Result
from .template import Template
from .template_category import TemplateCategory
from .token import Token


Template.model_rebuild()


__all__ = [
    "EmailDetail",
    "Addressbook",
    "AddressbookId",
    "AddressbookVariable",
    "CreateTemplateResult",
    "Result",
    "Template",
    "TemplateCategory",
    "Token",
]
