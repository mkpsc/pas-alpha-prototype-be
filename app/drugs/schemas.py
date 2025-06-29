import uuid
from datetime import date
from app.fields import BaseCamelModel


class DrugIn(BaseCamelModel):
    name: str
    code: str
    description: str | None = None


class DrugOut(BaseCamelModel):
    id: uuid.UUID
    name: str
    code: str
    description: str | None = None


class CommissioningBodyDrugAssociationIn(BaseCamelModel):
    commissioning_body_id: str
    drug_id: str
    association_date: date | None = None


class CommissioningBodyDrugAssociationOut(BaseCamelModel):
    id: uuid.UUID
    commissioning_body_id: str
    drug_id: str
    association_date: date
