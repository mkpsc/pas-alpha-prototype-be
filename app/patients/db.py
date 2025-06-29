from typing import Any
from app.database import database, patients, patient_transfers
from sqlalchemy import select, insert, update
from databases.backends.common.records import Record


async def select_patient(nhs_number: str) -> Record | None:
    return await database.fetch_one(
        select(patients).where(patients.c.nhs_number == nhs_number)
    )


async def select_all_patients() -> list[Record]:
    return await database.fetch_all(select(patients))


async def insert_patient(patient_data: dict[str, Any]) -> None:
    await database.execute(insert(patients).values(patient_data))


async def update_patient(nhs_number: str, patient_data: dict[str, Any]) -> None:
    await database.execute(
        update(patients).where(patients.c.nhs_number == nhs_number).values(patient_data)
    )


async def insert_patient_transfer(transfer_data: dict[str, Any]) -> None:
    await database.execute(insert(patient_transfers).values(transfer_data))
