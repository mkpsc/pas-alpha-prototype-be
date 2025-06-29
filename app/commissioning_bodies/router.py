from fastapi import APIRouter, HTTPException, status
from app.commissioning_bodies import controller
from app.commissioning_bodies.schemas import CommissioningBodyIn, CommissioningBodyOut

router = APIRouter(prefix="/commissioning-bodies", tags=["commissioning-bodies"])


@router.get("/{commissioning_body_id}", response_model=CommissioningBodyOut)
async def get_commissioning_body(commissioning_body_id: str):
    try:
        return await controller.get_commissioning_body(commissioning_body_id)
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/", response_model=list[CommissioningBodyOut])
async def get_all_commissioning_bodies():
    return await controller.get_all_commissioning_bodies()


@router.post("/", response_model=CommissioningBodyOut)
async def create_commissioning_body(commissioning_body: CommissioningBodyIn):
    return await controller.create_commissioning_body(commissioning_body)


@router.put("/{commissioning_body_id}", response_model=CommissioningBodyOut)
async def update_commissioning_body(
    commissioning_body_id: str, commissioning_body: CommissioningBodyIn
):
    try:
        return await controller.update_commissioning_body(
            commissioning_body_id, commissioning_body
        )
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
