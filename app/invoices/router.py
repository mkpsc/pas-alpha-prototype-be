from fastapi import APIRouter, HTTPException
from app.invoices import controller
from app.invoices.schemas import InvoiceIn, InvoiceOut, InvoiceMatchIn


router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.get("/{invoice_id}", response_model=InvoiceOut)
async def get_invoice(invoice_id: str):
    try:
        return await controller.get_invoice(invoice_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[InvoiceOut])
async def get_all_invoices():
    return await controller.get_all_invoices()


@router.post("/", response_model=InvoiceOut)
async def create_invoice(invoice: InvoiceIn):
    return await controller.create_invoice(invoice)


@router.put("/{invoice_id}", response_model=InvoiceOut)
async def update_invoice(invoice_id: str, invoice: InvoiceIn):
    try:
        return await controller.update_invoice(invoice_id, invoice)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/match")
async def match_invoice_to_request(match: InvoiceMatchIn):
    try:
        return await controller.match_invoice_to_request(match)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
