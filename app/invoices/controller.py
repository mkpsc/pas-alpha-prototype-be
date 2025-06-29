import uuid
from app.invoices import db
from app.invoices.schemas import InvoiceIn, InvoiceOut, InvoiceMatchIn


async def create_invoice(invoice: InvoiceIn) -> InvoiceOut:
    invoice_data = invoice.model_dump()
    invoice_data["id"] = str(uuid.uuid4())
    await db.insert_invoice(invoice_data)
    return InvoiceOut(**invoice_data)


async def get_invoice(invoice_id: str) -> InvoiceOut:
    invoice = await db.select_invoice(invoice_id)
    if not invoice:
        raise KeyError(f"Invoice with ID {invoice_id} not found")
    return InvoiceOut(**invoice._mapping)


async def get_all_invoices() -> list[InvoiceOut]:
    invoices = await db.select_all_invoices()
    return [InvoiceOut(**invoice._mapping) for invoice in invoices]


async def update_invoice(invoice_id: str, invoice: InvoiceIn) -> InvoiceOut:
    existing_invoice = await db.select_invoice(invoice_id)
    if not existing_invoice:
        raise KeyError(f"Invoice with ID {invoice_id} not found")

    invoice_data = invoice.model_dump()
    await db.update_invoice(invoice_id, invoice_data)
    updated_invoice = await db.select_invoice(invoice_id)
    return InvoiceOut(**updated_invoice._mapping)


async def match_invoice_to_request(match: InvoiceMatchIn) -> dict:
    invoice = await db.select_invoice(match.invoiceId)
    if not invoice:
        raise KeyError(f"Invoice with ID {match.invoiceId} not found")

    request = await db.select_request_by_id(match.requestId)
    if not request:
        raise KeyError(f"Request with ID {match.requestId} not found")

    match_data = {
        "id": str(uuid.uuid4()),
        "invoice_id": match.invoiceId,
        "request_id": match.requestId,
        "match_date": match.matchDate,
    }

    await db.insert_invoice_match(match_data)
    return {"message": "Invoice matched to request successfully"}
