from pydantic import BaseModel

from app.fields import NHSNumber


class PatientIn(BaseModel):
    initials: str
    nhs_number: NHSNumber


class PatientOut(BaseModel):
    initials: str
    nhs_number: NHSNumber
