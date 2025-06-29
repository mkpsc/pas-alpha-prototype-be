import uuid
from enum import Enum
from app.fields import BaseCamelModel


class FormStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DRAFT = "draft"


class QuestionType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    DATE = "date"
    SELECT = "select"
    MULTISELECT = "multiselect"
    BOOLEAN = "boolean"


class FormIn(BaseCamelModel):
    title: str
    status: FormStatus


class FormOut(BaseCamelModel):
    id: uuid.UUID
    title: str
    status: FormStatus


class QuestionIn(BaseCamelModel):
    text: str
    type: QuestionType
    options: list[str] | None = None


class QuestionOut(BaseCamelModel):
    id: uuid.UUID
    form_id: uuid.UUID
    text: str
    type: QuestionType
    options: list[str] | None = None
