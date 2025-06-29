import uuid

from asyncpg import UniqueViolationError
from app.patients import db
from app.patients.exceptions import PatientAlreadyExistsError, PatientNotFoundError
from app.patients.schemas import PatientIn, PatientOut, PatientTransfer


async def get_patient(nhs_number: str) -> PatientOut:
    record = await db.select_patient(nhs_number)
    if not record:
        raise KeyError(f"Patient with NHS number {nhs_number} not found")
    return PatientOut(**record)


async def get_all_patients() -> list[PatientOut]:
    records = await db.select_all_patients()
    return [PatientOut(**record) for record in records]


async def create_patient(patient_in: PatientIn) -> PatientOut:
    patient_data = patient_in.model_dump()
    patient_data["id"] = str(uuid.uuid4())
    try:
        await db.insert_patient(patient_data)
    except UniqueViolationError:
        raise PatientAlreadyExistsError(
            f"Patient with NHS number {patient_in.nhs_number} already exists"
        )
    return PatientOut(**patient_data)


async def update_patient(nhs_number: str, patient: PatientIn) -> PatientOut:
    existing_patient = await db.select_patient(nhs_number)
    if not existing_patient:
        raise PatientNotFoundError(f"Patient with NHS number {nhs_number} not found")

    patient_data = patient.model_dump()
    await db.update_patient(nhs_number, patient_data)
    updated_patient = await db.select_patient(nhs_number)
    return PatientOut(**updated_patient._mapping)


async def transfer_patient(transfer: PatientTransfer) -> dict:
    patient = await db.select_patient(transfer.patientNhsNumber)
    if not patient:
        raise PatientNotFoundError(
            f"Patient with NHS number {transfer.patientNhsNumber} not found"
        )

    transfer_data = {
        "id": str(uuid.uuid4()),
        "patient_nhs_number": transfer.patientNhsNumber,
        "from_provider_id": transfer.fromProviderId,
        "to_provider_id": transfer.toProviderId,
        "transfer_date": transfer.transferDate,
        "reason": transfer.reason,
    }

    await db.insert_patient_transfer(transfer_data)
    return {"message": "Patient transfer recorded successfully"}
