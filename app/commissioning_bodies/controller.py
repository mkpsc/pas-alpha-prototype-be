import uuid
from app.commissioning_bodies import db
from app.commissioning_bodies.schemas import CommissioningBodyIn, CommissioningBodyOut


async def get_commissioning_body(commissioning_body_id: str) -> CommissioningBodyOut:
    commissioning_body = await db.select_commissioning_body(commissioning_body_id)
    if not commissioning_body:
        raise KeyError(f"Commissioning body with ID {commissioning_body_id} not found")
    return CommissioningBodyOut(**commissioning_body._mapping)


async def get_all_commissioning_bodies() -> list[CommissioningBodyOut]:
    commissioning_bodies = await db.select_all_commissioning_bodies()
    return [CommissioningBodyOut(**cb._mapping) for cb in commissioning_bodies]


async def create_commissioning_body(
    commissioning_body: CommissioningBodyIn,
) -> CommissioningBodyOut:
    commissioning_body_data = commissioning_body.model_dump()
    commissioning_body_data["id"] = str(uuid.uuid4())
    await db.insert_commissioning_body(commissioning_body_data)
    return CommissioningBodyOut(**commissioning_body_data)


async def update_commissioning_body(
    commissioning_body_id: str, commissioning_body: CommissioningBodyIn
) -> CommissioningBodyOut:
    existing_commissioning_body = await db.select_commissioning_body(
        commissioning_body_id
    )
    if not existing_commissioning_body:
        raise KeyError(f"Commissioning body with ID {commissioning_body_id} not found")

    commissioning_body_data = commissioning_body.model_dump()
    await db.update_commissioning_body(commissioning_body_id, commissioning_body_data)
    updated_commissioning_body = await db.select_commissioning_body(
        commissioning_body_id
    )
    return CommissioningBodyOut(**updated_commissioning_body._mapping)
