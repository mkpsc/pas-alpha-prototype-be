import uuid
from app.requests import db
from app.requests.schemas import (
    RequestIn,
    RequestOut,
    CommunicationIn,
    CommunicationOut,
    ContinuationRequestIn,
    ContinuationRequestOut,
    RequestStatus,
)


async def get_request(request_id: uuid.UUID) -> RequestOut:
    request = await db.select_request(request_id)
    if not request:
        raise KeyError(f"Request with ID {request_id} not found")
    return RequestOut(**request._mapping)


async def get_all_requests() -> list[RequestOut]:
    requests = await db.select_all_requests()
    return [RequestOut(**request._mapping) for request in requests]


async def create_request(request: RequestIn) -> RequestOut:
    request_data = request.model_dump()
    request_data["id"] = uuid.uuid4()
    request_data["status"] = RequestStatus.PENDING
    await db.insert_request(request_data)
    return RequestOut(**request_data)


async def update_request(request_id: uuid.UUID, request: RequestIn) -> RequestOut:
    existing_request = await db.select_request(request_id)
    if not existing_request:
        raise KeyError(f"Request with ID {request_id} not found")

    request_data = request.model_dump()
    await db.update_request(request_id, request_data)
    updated_request = await db.select_request(request_id)
    return RequestOut(**updated_request._mapping)


async def update_request_status(request_id: uuid.UUID, status: RequestStatus) -> None:
    existing_request = await db.select_request(request_id)
    if not existing_request:
        raise KeyError(f"Request with ID {request_id} not found")

    await db.update_request_status(request_id, status)


async def get_request_communications(request_id: uuid.UUID) -> list[CommunicationOut]:
    communications = await db.select_request_communications(request_id)
    return [CommunicationOut(**comm._mapping) for comm in communications]


async def create_communication(communication: CommunicationIn) -> CommunicationOut:
    communication_data = communication.model_dump()
    communication_data["id"] = uuid.uuid4()
    await db.insert_communication(communication_data)
    return CommunicationOut(**communication_data)


async def create_continuation_request(
    continuation: ContinuationRequestIn,
) -> ContinuationRequestOut:
    continuation_data = continuation.model_dump()
    continuation_data["id"] = uuid.uuid4()
    await db.insert_continuation_request(continuation_data)
    return ContinuationRequestOut(**continuation_data)
