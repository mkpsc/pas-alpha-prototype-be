from app.database import database, requests, communications, continuation_requests
from sqlalchemy import select, insert, update


async def select_request(request_id: str):
    return await database.fetch_one(select(requests).where(requests.c.id == request_id))


async def select_all_requests():
    return await database.fetch_all(select(requests))


async def insert_request(request_data: dict) -> None:
    await database.execute(insert(requests).values(request_data))


async def update_request(request_id: str, request_data: dict) -> None:
    await database.execute(
        update(requests).where(requests.c.id == request_id).values(request_data)
    )


async def update_request_status(request_id: str, status: str) -> None:
    await database.execute(
        update(requests).where(requests.c.id == request_id).values(status=status)
    )


async def select_request_communications(request_id: str):
    return await database.fetch_all(
        select(communications).where(communications.c.request_id == request_id)
    )


async def insert_communication(communication_data: dict) -> None:
    await database.execute(insert(communications).values(communication_data))


async def insert_continuation_request(continuation_data: dict) -> None:
    await database.execute(insert(continuation_requests).values(continuation_data))
