from fastapi import APIRouter, HTTPException
from app.drugs import controller
from app.drugs.schemas import (
    DrugOut,
    CommissioningBodyDrugAssociationIn,
)

router = APIRouter(prefix="/drugs", tags=["drugs"])


@router.get("/{drug_id}", response_model=DrugOut)
async def get_drug(drug_id: str):
    try:
        return await controller.get_drug(drug_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[DrugOut])
async def get_all_drugs():
    return await controller.get_all_drugs()


@router.get("/commissioning-bodies/{commissioning_body_id}")
async def get_commissioning_body_drugs(commissioning_body_id: str):
    return await controller.get_commissioning_body_drugs(commissioning_body_id)


@router.post("/associations")
async def associate_drug_with_commissioning_body(
    association: CommissioningBodyDrugAssociationIn,
):
    try:
        return await controller.associate_drug_with_commissioning_body(association)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
