import uuid
from datetime import date
from app.fields import BaseCamelModel


class ProviderIn(BaseCamelModel):
    name: str


class ProviderOut(BaseCamelModel):
    id: uuid.UUID
    name: str


class ClinicianProviderAssociationIn(BaseCamelModel):
    clinician_id: str
    provider_id: str
    association_date: date | None = None


class ClinicianProviderAssociationOut(BaseCamelModel):
    id: uuid.UUID
    clinician_id: str
    provider_id: str
    association_date: date


class ClinicianIn(BaseCamelModel):
    first_name: str
    last_name: str


class ClinicianOut(BaseCamelModel):
    id: uuid.UUID
    first_name: str
    last_name: str
