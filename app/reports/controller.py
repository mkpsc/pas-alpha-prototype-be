import uuid
from app.reports import db
from app.commissioning_bodies import db as commissioning_bodies_db
from app.reports.schemas import (
    CommissioningBodyReportAssociationIn,
    ProviderReportAssociationIn,
)


async def get_commissioning_body_reports(commissioning_body_id: str) -> list[dict]:
    associations = await db.select_commissioning_body_reports(commissioning_body_id)
    result = []

    for assoc in associations:
        report = await db.select_report(assoc.report_id)
        if report:
            result.append(
                {
                    "reportId": report.id,
                    "reportName": report.name,
                    "reportType": report.type,
                    "associationDate": assoc.association_date,
                }
            )

    return result


async def get_provider_reports(provider_id: str) -> list[dict]:
    associations = await db.select_provider_reports(provider_id)
    result = []

    for assoc in associations:
        report = await db.select_report(assoc.report_id)
        if report:
            result.append(
                {
                    "reportId": report.id,
                    "reportName": report.name,
                    "reportType": report.type,
                    "associationDate": assoc.association_date,
                }
            )

    return result


async def associate_report_with_commissioning_body(
    association: CommissioningBodyReportAssociationIn,
) -> dict:
    commissioning_body = await commissioning_bodies_db.select_commissioning_body(
        association.commissioningBodyId
    )
    if not commissioning_body:
        raise KeyError(
            f"Commissioning body with ID {association.commissioningBodyId} not found"
        )

    association_data = {
        "id": str(uuid.uuid4()),
        "commissioning_body_id": association.commissioningBodyId,
        "report_id": association.reportId,
        "association_date": association.associationDate,
    }

    await db.insert_commissioning_body_report(association_data)
    return {"message": "Report associated with commissioning body successfully"}


async def associate_report_with_provider(
    association: ProviderReportAssociationIn,
) -> dict:
    association_data = {
        "id": str(uuid.uuid4()),
        "provider_id": association.providerId,
        "report_id": association.reportId,
        "association_date": association.associationDate,
    }

    await db.insert_provider_report(association_data)
    return {"message": "Report associated with provider successfully"}
