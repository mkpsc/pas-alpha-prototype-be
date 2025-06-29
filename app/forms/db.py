from app.database import database, forms, questions
from sqlalchemy import select, insert, update
import uuid


async def select_form(form_id: uuid.UUID):
    return await database.fetch_one(select(forms).where(forms.c.id == form_id))


async def select_all_forms():
    return await database.fetch_all(select(forms))


async def insert_form(form_data: dict) -> None:
    await database.execute(insert(forms).values(form_data))


async def update_form(form_id: uuid.UUID, form_data: dict) -> None:
    await database.execute(update(forms).where(forms.c.id == form_id).values(form_data))


async def select_form_questions(form_id: uuid.UUID):
    return await database.fetch_all(
        select(questions).where(questions.c.form_id == form_id)
    )


async def insert_question(form_id: uuid.UUID, question_data: dict) -> None:
    question_data["form_id"] = form_id
    question_data["id"] = uuid.uuid4()
    await database.execute(insert(questions).values(question_data))


async def select_question(question_id: uuid.UUID):
    return await database.fetch_one(
        select(questions).where(questions.c.id == question_id)
    )


async def update_question(question_id: uuid.UUID, question_data: dict) -> None:
    await database.execute(
        update(questions).where(questions.c.id == question_id).values(question_data)
    )
