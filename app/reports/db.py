from app.database import (
    database,
    commissioning_body_reports,
    provider_reports,
    reports,
)
from sqlalchemy import select, insert


async def select_commissioning_body_reports(commissioning_body_id: str):
    return await database.fetch_all(
        select(commissioning_body_reports).where(
            commissioning_body_reports.c.commissioning_body_id == commissioning_body_id
        )
    )


async def select_provider_reports(provider_id: str):
    return await database.fetch_all(
        select(provider_reports).where(provider_reports.c.provider_id == provider_id)
    )


async def select_report(report_id: str):
    return await database.fetch_one(select(reports).where(reports.c.id == report_id))


async def insert_commissioning_body_report(association_data: dict) -> None:
    await database.execute(insert(commissioning_body_reports).values(association_data))


async def insert_provider_report(association_data: dict) -> None:
    await database.execute(insert(provider_reports).values(association_data))
