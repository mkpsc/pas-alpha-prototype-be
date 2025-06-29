from app.database import database, commissioning_bodies
from sqlalchemy import select, insert, update


async def select_commissioning_body(commissioning_body_id: str):
    return await database.fetch_one(
        select(commissioning_bodies).where(
            commissioning_bodies.c.id == commissioning_body_id
        )
    )


async def select_all_commissioning_bodies():
    return await database.fetch_all(select(commissioning_bodies))


async def insert_commissioning_body(commissioning_body_data: dict) -> None:
    await database.execute(insert(commissioning_bodies).values(commissioning_body_data))


async def update_commissioning_body(
    commissioning_body_id: str, commissioning_body_data: dict
) -> None:
    await database.execute(
        update(commissioning_bodies)
        .where(commissioning_bodies.c.id == commissioning_body_id)
        .values(commissioning_body_data)
    )
