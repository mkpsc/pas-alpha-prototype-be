import uuid
from fastapi import APIRouter, HTTPException, Response, status
from app.requests import controller
from app.requests.schemas import (
    RequestIn,
    RequestOut,
    ContinuationRequestIn,
    ContinuationRequestOut,
    CommunicationIn,
    CommunicationOut,
    RequestStatus,
)


router = APIRouter(prefix="/requests", tags=["requests"])


@router.get("/{request_id}", response_model=RequestOut)
async def get_request(request_id: str):
    try:
        return await controller.get_request(request_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[RequestOut])
async def get_all_requests():
    return await controller.get_all_requests()


@router.post("/", response_model=RequestOut)
async def create_request(request: RequestIn):
    return await controller.create_request(request)


@router.put("/{request_id}", response_model=RequestOut)
async def update_request(request_id: str, request: RequestIn):
    try:
        return await controller.update_request(request_id, request)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{request_id}/status", status_code=status.HTTP_204_NO_CONTENT)
async def update_request_status(request_id: uuid.UUID, request_status: RequestStatus):
    try:
        await controller.update_request_status(request_id, request_status)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{request_id}/communications", response_model=list[CommunicationOut])
async def get_request_communications(request_id: str):
    return await controller.get_request_communications(request_id)


@router.post("/communications", response_model=CommunicationOut)
async def create_communication(communication: CommunicationIn):
    return await controller.create_communication(communication)


@router.post("/continuations", response_model=ContinuationRequestOut)
async def create_continuation_request(continuation: ContinuationRequestIn):
    return await controller.create_continuation_request(continuation)
