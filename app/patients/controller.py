from app.patients.schemas import PatientIn
from app.database import DB


def create_patient(patient: PatientIn) -> None:
    DB["patients"][patient.nhs_number] = patient
    return patient


def get_patient(nhs_number: str) -> PatientIn:
    return DB["patients"][nhs_number]
