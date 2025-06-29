from app.providers import db
import uuid
from app.providers.schemas import ClinicianProviderAssociationIn


async def get_clinician_providers(clinician_id: str) -> list[dict]:
    associations = await db.select_clinician_providers(clinician_id)
    result = []

    for assoc in associations:
        provider = await db.select_provider(assoc.provider_id)
        if provider:
            result.append(
                {
                    "providerId": provider.id,
                    "providerName": provider.name,
                    "associationDate": assoc.association_date,
                }
            )

    return result


async def associate_clinician_with_provider(
    association: ClinicianProviderAssociationIn,
) -> dict:
    association_data = {
        "id": str(uuid.uuid4()),
        "clinician_id": association.clinicianId,
        "provider_id": association.providerId,
        "association_date": association.associationDate,
    }

    await db.insert_clinician_provider(association_data)
    return {"message": "Clinician associated with provider successfully"}


async def get_provider_clinicians(provider_id: str) -> list[dict]:
    associations = await db.select_provider_clinicians(provider_id)
    result = []

    for assoc in associations:
        clinician = await db.select_clinician(assoc.clinician_id)
        if clinician:
            result.append(
                {
                    "clinicianId": clinician.id,
                    "clinicianName": f"{clinician.first_name} {clinician.last_name}",
                    "associationDate": assoc.association_date,
                }
            )

    return result
