import uuid
from enum import Enum
from datetime import datetime
from app.fields import BaseCamelModel


class InvoiceStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    REJECTED = "rejected"


class InvoiceIn(BaseCamelModel):
    amount: float
    submission_date: datetime | None = None
    status: InvoiceStatus


class InvoiceOut(BaseCamelModel):
    id: uuid.UUID
    amount: float
    submission_date: datetime
    status: InvoiceStatus


class InvoiceMatchIn(BaseCamelModel):
    invoice_id: str
    request_id: str
    match_date: datetime | None = None


class InvoiceMatchOut(BaseCamelModel):
    id: uuid.UUID
    invoice_id: str
    request_id: str
    match_date: datetime
