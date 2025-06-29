from fastapi import APIRouter
from app.reports import controller
from app.reports.schemas import (
    CommissioningBodyReportAssociationIn,
    ProviderReportAssociationIn,
)

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/commissioning-bodies/{commissioning_body_id}")
async def get_commissioning_body_reports(commissioning_body_id: str):
    return await controller.get_commissioning_body_reports(commissioning_body_id)


@router.get("/providers/{provider_id}")
async def get_provider_reports(provider_id: str):
    return await controller.get_provider_reports(provider_id)


@router.post("/commissioning-body-associations")
async def associate_report_with_commissioning_body(
    association: CommissioningBodyReportAssociationIn,
):
    return await controller.associate_report_with_commissioning_body(association)


@router.post("/provider-associations")
async def associate_report_with_provider(association: ProviderReportAssociationIn):
    return await controller.associate_report_with_provider(association)
