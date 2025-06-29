import uuid
from datetime import date
from app.fields import BaseCamelModel


class ReportIn(BaseCamelModel):
    name: str
    type: str
    content: str | None = None


class ReportOut(BaseCamelModel):
    id: uuid.UUID
    name: str
    type: str
    content: str | None = None


class CommissioningBodyReportAssociationIn(BaseCamelModel):
    commissioning_body_id: str
    report_id: str
    association_date: date | None = None


class CommissioningBodyReportAssociationOut(BaseCamelModel):
    id: uuid.UUID
    commissioning_body_id: str
    report_id: str
    association_date: date


class ProviderReportAssociationIn(BaseCamelModel):
    provider_id: str
    report_id: str
    association_date: date | None = None


class ProviderReportAssociationOut(BaseCamelModel):
    id: uuid.UUID
    provider_id: str
    report_id: str
    association_date: date
