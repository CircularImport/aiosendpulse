from .email import EmailDetail
from .result import CreateTemplateResult, Result
from .template import Template
from .template_category import TemplateCategory
from .token import Token


Template.model_rebuild()


__all__ = [
    "EmailDetail",
    "CreateTemplateResult",
    "Result",
    "Template",
    "TemplateCategory",
    "Token",
]
