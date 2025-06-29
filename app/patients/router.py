from fastapi import APIRouter, HTTPException, status
from app.patients import controller
from app.patients.exceptions import PatientAlreadyExistsError
from app.patients.schemas import PatientIn, PatientOut, PatientTransfer


router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/{nhs_number}", response_model=PatientOut)
async def get_patient(nhs_number: str):
    try:
        return await controller.get_patient(nhs_number)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[PatientOut])
async def get_all_patients():
    return await controller.get_all_patients()


@router.post("/", response_model=PatientOut)
async def create_patient(patient: PatientIn):
    try:
        return await controller.create_patient(patient)
    except PatientAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put("/{nhs_number}", response_model=PatientOut)
async def update_patient(nhs_number: str, patient: PatientIn):
    try:
        return await controller.update_patient(nhs_number, patient)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/transfer")
async def transfer_patient(transfer: PatientTransfer):
    try:
        return await controller.transfer_patient(transfer)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
