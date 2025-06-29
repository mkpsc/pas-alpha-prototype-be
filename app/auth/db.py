from app.database import database
from app.database import invalidated_tokens
from sqlalchemy import insert


async def insert_invalidated_token(token_data: dict) -> None:
    await database.execute(insert(invalidated_tokens).values(token_data))
