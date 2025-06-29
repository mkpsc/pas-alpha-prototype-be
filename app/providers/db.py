from app.database import database, clinician_providers, providers, clinicians
from sqlalchemy import select, insert


async def select_clinician_providers(clinician_id: str):
    return await database.fetch_all(
        select(clinician_providers).where(
            clinician_providers.c.clinician_id == clinician_id
        )
    )


async def select_provider(provider_id: str):
    return await database.fetch_one(
        select(providers).where(providers.c.id == provider_id)
    )


async def insert_clinician_provider(association_data: dict) -> None:
    await database.execute(insert(clinician_providers).values(association_data))


async def select_provider_clinicians(provider_id: str):
    return await database.fetch_all(
        select(clinician_providers).where(
            clinician_providers.c.provider_id == provider_id
        )
    )


async def select_clinician(clinician_id: str):
    return await database.fetch_one(
        select(clinicians).where(clinicians.c.id == clinician_id)
    )
