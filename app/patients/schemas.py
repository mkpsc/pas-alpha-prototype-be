from datetime import date

import uuid
from app.fields import BaseCamelModel, NHSNumber


class PatientIn(BaseCamelModel):
    nhs_number: NHSNumber
    first_name: str
    last_name: str
    date_of_birth: date | None = None


class PatientOut(BaseCamelModel):
    id: uuid.UUID
    nhs_number: NHSNumber
    first_name: str
    last_name: str
    date_of_birth: date | None = None


class PatientTransfer(BaseCamelModel):
    patient_nhs_number: NHSNumber
    from_provider_id: str
    to_provider_id: str
    transfer_date: date
    reason: str
