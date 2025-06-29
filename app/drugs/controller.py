import uuid
from app.drugs import db
from app.commissioning_bodies import db as commissioning_bodies_db
from app.drugs.schemas import DrugOut, CommissioningBodyDrugAssociationIn


async def get_drug(drug_id: str) -> DrugOut:
    drug = await db.select_drug(drug_id)
    if not drug:
        raise KeyError(f"Drug with ID {drug_id} not found")
    return DrugOut(**drug._mapping)


async def get_all_drugs() -> list[DrugOut]:
    drugs = await db.select_all_drugs()
    return [DrugOut(**drug._mapping) for drug in drugs]


async def get_commissioning_body_drugs(commissioning_body_id: str) -> list[dict]:
    drug_ids = await db.select_commissioning_body_drugs(commissioning_body_id)
    result = []

    for drug_id_row in drug_ids:
        drug = await db.select_drug(drug_id_row.drug_id)
        if drug:
            result.append(
                {
                    "drugId": drug.id,
                    "drugName": drug.name,
                    "drugCode": drug.code,
                }
            )

    return result


async def associate_drug_with_commissioning_body(
    association: CommissioningBodyDrugAssociationIn,
) -> dict:
    commissioning_body = await commissioning_bodies_db.select_commissioning_body(
        association.commissioningBodyId
    )
    if not commissioning_body:
        raise KeyError(
            f"Commissioning body with ID {association.commissioningBodyId} not found"
        )

    drug = await db.select_drug(association.drugId)
    if not drug:
        raise KeyError(f"Drug with ID {association.drugId} not found")

    association_data = {
        "id": str(uuid.uuid4()),
        "commissioning_body_id": association.commissioningBodyId,
        "drug_id": association.drugId,
        "association_date": association.associationDate,
    }

    await db.insert_commissioning_body_drug(association_data)
    return {"message": "Drug associated with commissioning body successfully"}
