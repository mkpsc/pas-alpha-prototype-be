from typing import AsyncIterator
from fastapi import FastAPI
from app.patients.router import router as patients_router
from app.auth.router import router as auth_router
from app.forms.router import router as forms_router
from app.requests.router import router as requests_router
from app.invoices.router import router as invoices_router
from app.providers.router import router as providers_router
from app.drugs.router import router as drugs_router
from app.reports.router import router as reports_router
from app.commissioning_bodies.router import router as commissioning_bodies_router
from app.database import create_tables, database
import uvicorn


async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    await create_tables()
    yield
    await database.disconnect()


app = FastAPI(
    title="NHS England Prior Approval Management System API",
    version="0.1.0",
    description="Fully comprehensive API specification supporting complete user journeys including invoices, dynamic forms, requests, and communications.",
    lifespan=lifespan,
)


app.include_router(auth_router)
app.include_router(patients_router)
app.include_router(forms_router)
app.include_router(requests_router)
app.include_router(invoices_router)
app.include_router(providers_router)
app.include_router(drugs_router)
app.include_router(reports_router)
app.include_router(commissioning_bodies_router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
