from pydantic import BaseModel


class PatientIn(BaseModel):
    initials: str
    nhs_number: str


class PatientOut(BaseModel):
    initials: str
    nhs_number: str
