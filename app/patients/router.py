from fastapi import APIRouter, HTTPException, Response, status
from app.database import DB
from app.patients import controller
from app.patients.schemas import PatientIn, PatientOut


router = APIRouter()


@router.get("/")
async def get_patients() -> list[PatientOut]:
    return list(DB["patients"].values())


@router.get("/{nhs_number}")
async def get_patient(nhs_number: str) -> PatientOut:
    try:
        return controller.get_patient(nhs_number)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/")
async def post_patient(patient: PatientIn) -> Response:
    controller.create_patient(patient)
    return Response(status_code=status.HTTP_201_CREATED)
