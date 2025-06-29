from app.database import (
    database,
    drugs,
    commissioning_body_drugs,
    commissioning_bodies,
)
from sqlalchemy import select, insert


async def select_drug(drug_id: str):
    return await database.fetch_one(select(drugs).where(drugs.c.id == drug_id))


async def select_all_drugs():
    return await database.fetch_all(select(drugs))


async def select_commissioning_body_drugs(commissioning_body_id: str):
    return await database.fetch_all(
        select(commissioning_body_drugs.c.drug_id).where(
            commissioning_body_drugs.c.commissioning_body_id == commissioning_body_id
        )
    )


async def select_commissioning_body(commissioning_body_id: str):
    return await database.fetch_one(
        select(commissioning_bodies).where(
            commissioning_bodies.c.id == commissioning_body_id
        )
    )


async def insert_commissioning_body_drug(association_data: dict) -> None:
    await database.execute(insert(commissioning_body_drugs).values(association_data))
