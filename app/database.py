import os
from databases import Database
from sqlalchemy import (
    UUID,
    MetaData,
    Table,
    Column,
    String,
    DateTime,
    Date,
    Numeric,
    Text,
    ARRAY,
    ForeignKey,
)
import sqlalchemy
from sqlalchemy.sql import func
import uuid


database = Database(
    os.getenv(
        "DATABASE_URL", "postgresql://pas_user:pas_password@localhost:5032/pas_alpha"
    )
)
metadata = MetaData()

patients = Table(
    "patients",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("nhs_number", String(10), unique=True, nullable=False, index=True),
    Column("first_name", String(100), nullable=False),
    Column("last_name", String(100), nullable=False),
    Column("date_of_birth", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

forms = Table(
    "forms",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("title", String(200), nullable=False),
    Column("status", String(20), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

questions = Table(
    "questions",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("form_id", UUID, ForeignKey("forms.id"), nullable=False),
    Column("text", Text, nullable=False),
    Column("type", String(20), nullable=False),
    Column("options", ARRAY(String), nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

requests = Table(
    "requests",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("treatment_id", String(100), nullable=False),
    Column("form_id", UUID, ForeignKey("forms.id"), nullable=False),
    Column("status", String(20), nullable=False),
    Column("submission_date", DateTime(timezone=True), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

communications = Table(
    "communications",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("request_id", UUID, ForeignKey("requests.id"), nullable=False),
    Column("type", String(20), nullable=False),
    Column("sent_date", DateTime(timezone=True), nullable=False),
    Column("recipient", String(200), nullable=False),
    Column("content", Text, nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

continuation_requests = Table(
    "continuation_requests",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("original_request_id", UUID, ForeignKey("requests.id"), nullable=False),
    Column("reason", Text, nullable=False),
    Column("type", String(20), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

invoices = Table(
    "invoices",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("submission_date", DateTime(timezone=True), nullable=False),
    Column("status", String(20), nullable=False),
    Column("matched_request_ids", ARRAY(String), nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

providers = Table(
    "providers",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("name", String(200), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

clinicians = Table(
    "clinicians",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("first_name", String(100), nullable=False),
    Column("last_name", String(100), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

clinician_providers = Table(
    "clinician_providers",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("clinician_id", UUID, ForeignKey("clinicians.id"), nullable=False),
    Column("provider_id", UUID, ForeignKey("providers.id"), nullable=False),
    Column("association_date", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

commissioning_bodies = Table(
    "commissioning_bodies",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("name", String(200), nullable=False),
    Column("code", String(50), unique=True, nullable=False),
    Column("description", Text, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

drugs = Table(
    "drugs",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("name", String(200), nullable=False),
    Column("code", String(100), unique=True, nullable=False),
    Column("description", Text, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

commissioning_body_drugs = Table(
    "commissioning_body_drugs",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column(
        "commissioning_body_id",
        UUID,
        ForeignKey("commissioning_bodies.id"),
        nullable=False,
    ),
    Column("drug_id", UUID, ForeignKey("drugs.id"), nullable=False),
    Column("association_date", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

reports = Table(
    "reports",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("name", String(200), nullable=False),
    Column("type", String(50), nullable=False),
    Column("content", Text, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

commissioning_body_reports = Table(
    "commissioning_body_reports",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column(
        "commissioning_body_id",
        UUID,
        ForeignKey("commissioning_bodies.id"),
        nullable=False,
    ),
    Column("report_id", UUID, ForeignKey("reports.id"), nullable=False),
    Column("association_date", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

provider_reports = Table(
    "provider_reports",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("provider_id", UUID, ForeignKey("providers.id"), nullable=False),
    Column("report_id", UUID, ForeignKey("reports.id"), nullable=False),
    Column("association_date", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

patient_transfers = Table(
    "patient_transfers",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("patient_nhs_number", String(10), nullable=False),
    Column("from_provider_id", UUID, ForeignKey("providers.id"), nullable=False),
    Column("to_provider_id", UUID, ForeignKey("providers.id"), nullable=False),
    Column("transfer_date", Date, nullable=False),
    Column("reason", Text, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

invoice_matches = Table(
    "invoice_matches",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("invoice_id", UUID, ForeignKey("invoices.id"), nullable=False),
    Column("request_id", UUID, ForeignKey("requests.id"), nullable=False),
    Column("match_date", Date, nullable=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
)

invalidated_tokens = Table(
    "invalidated_tokens",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("token", String(500), nullable=False),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
)


async def create_tables():
    for table in metadata.tables.values():
        schema = sqlalchemy.schema.CreateTable(table, if_not_exists=True)
        query = str(schema.compile(dialect=sqlalchemy.dialects.postgresql.dialect()))
        await database.execute(query=query)
        await database.execute(sqlalchemy.schema.CreateTable(table, if_not_exists=True))
