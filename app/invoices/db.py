from app.database import database, invoices, requests, invoice_matches
from sqlalchemy import select, insert, update


async def select_invoice(invoice_id: str):
    return await database.fetch_one(select(invoices).where(invoices.c.id == invoice_id))


async def select_all_invoices():
    return await database.fetch_all(select(invoices))


async def insert_invoice(invoice_data: dict) -> None:
    await database.execute(insert(invoices).values(invoice_data))


async def update_invoice(invoice_id: str, invoice_data: dict) -> None:
    await database.execute(
        update(invoices).where(invoices.c.id == invoice_id).values(invoice_data)
    )


async def select_request_by_id(request_id: str):
    return await database.fetch_one(select(requests).where(requests.c.id == request_id))


async def insert_invoice_match(match_data: dict) -> None:
    await database.execute(insert(invoice_matches).values(match_data))
