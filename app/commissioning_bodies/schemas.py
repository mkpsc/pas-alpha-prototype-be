import uuid
from app.fields import BaseCamelModel


class CommissioningBodyIn(BaseCamelModel):
    name: str
    code: str
    description: str | None = None


class CommissioningBodyOut(BaseCamelModel):
    id: uuid.UUID
    name: str
    code: str
    description: str | None = None
