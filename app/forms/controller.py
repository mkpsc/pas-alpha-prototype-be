import uuid
from app.forms import db
from app.forms.schemas import FormIn, FormOut, QuestionIn, QuestionOut
from app.forms.exceptions import FormNotFoundError
from app.forms.exceptions import QuestionNotFoundError


async def get_form(form_id: uuid.UUID) -> FormOut:
    record = await db.select_form(form_id)
    if not record:
        raise FormNotFoundError(f"Form with ID {form_id} not found")
    return FormOut(**record)


async def get_all_forms() -> list[FormOut]:
    records = await db.select_all_forms()
    return [FormOut(**record) for record in records]


async def create_form(form: FormIn) -> FormOut:
    form_data = form.model_dump()
    form_data["id"] = str(uuid.uuid4())
    await db.insert_form(form_data)
    return FormOut(**form_data)


async def update_form(form_id: uuid.UUID, form: FormIn) -> FormOut:
    record = await db.select_form(form_id)
    if not record:
        raise FormNotFoundError(f"Form with ID {form_id} not found")

    form_data = form.model_dump()
    await db.update_form(form_id, form_data)
    updated_form = await db.select_form(form_id)
    return FormOut(**updated_form)


async def get_form_questions(form_id: uuid.UUID) -> list[QuestionOut]:
    records = await db.select_form_questions(form_id)
    return [QuestionOut(**record) for record in records]


async def create_question(form_id: uuid.UUID, question: QuestionIn) -> QuestionOut:
    question_data = question.model_dump()
    await db.insert_question(form_id, question_data)
    return QuestionOut(**question_data)


async def get_question(question_id: uuid.UUID) -> QuestionOut:
    record = await db.select_question(question_id)
    if not record:
        raise QuestionNotFoundError(f"Question with ID {question_id} not found")
    return QuestionOut(**record)


async def update_question(question_id: uuid.UUID, question: QuestionIn) -> QuestionOut:
    record = await db.select_question(question_id)
    if not record:
        raise QuestionNotFoundError(f"Question with ID {question_id} not found")

    question_data = question.model_dump()
    await db.update_question(question_id, question_data)
    updated_question = await db.select_question(question_id)
    return QuestionOut(**updated_question)
