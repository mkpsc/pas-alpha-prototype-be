import uuid
from enum import Enum
from datetime import datetime
from app.fields import BaseCamelModel


class RequestStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    IN_REVIEW = "in_review"


class CommunicationType(str, Enum):
    EMAIL = "email"
    LETTER = "letter"


class ContinuationType(str, Enum):
    CONTINUATION = "continuation"
    TREATMENT_BREAK = "treatment-break"


class RequestIn(BaseCamelModel):
    treatment_id: str
    form_id: uuid.UUID
    submission_date: datetime | None = None


class RequestOut(BaseCamelModel):
    id: uuid.UUID
    treatment_id: str
    form_id: uuid.UUID
    status: RequestStatus
    submission_date: datetime


class ContinuationRequestIn(BaseCamelModel):
    original_request_id: uuid.UUID
    reason: str
    type: ContinuationType


class ContinuationRequestOut(BaseCamelModel):
    id: uuid.UUID
    original_request_id: uuid.UUID
    reason: str
    type: ContinuationType


class CommunicationIn(BaseCamelModel):
    request_id: uuid.UUID
    type: CommunicationType
    sent_date: datetime | None = None
    recipient: str
    content: str


class CommunicationOut(BaseCamelModel):
    id: uuid.UUID
    request_id: uuid.UUID
    type: CommunicationType
    sent_date: datetime
    recipient: str
    content: str


class RequestStatusUpdate(BaseCamelModel):
    status: RequestStatus


class InvoiceMatch(BaseCamelModel):
    request_ids: list[uuid.UUID]
