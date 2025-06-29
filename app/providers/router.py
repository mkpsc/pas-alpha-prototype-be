from fastapi import APIRouter
from app.providers import controller
from app.providers.schemas import ClinicianProviderAssociationIn

router = APIRouter(prefix="/providers", tags=["providers"])


@router.get("/clinicians/{clinician_id}")
async def get_clinician_providers(clinician_id: str):
    return await controller.get_clinician_providers(clinician_id)


@router.post("/associations")
async def associate_clinician_with_provider(
    association: ClinicianProviderAssociationIn,
):
    return await controller.associate_clinician_with_provider(association)


@router.get("/{provider_id}/clinicians")
async def get_provider_clinicians(provider_id: str):
    return await controller.get_provider_clinicians(provider_id)
