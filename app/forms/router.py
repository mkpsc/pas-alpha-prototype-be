from fastapi import APIRouter, HTTPException, status
from app.forms import controller
from app.forms.exceptions import QuestionNotFoundError
from app.forms.exceptions import FormNotFoundError
from app.forms.schemas import FormIn, FormOut, QuestionIn, QuestionOut
import uuid

router = APIRouter(prefix="/forms", tags=["forms"])


@router.get("/{form_id}")
async def get_form(form_id: uuid.UUID) -> FormOut:
    try:
        return await controller.get_form(form_id)
    except FormNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/")
async def get_all_forms() -> list[FormOut]:
    return await controller.get_all_forms()


@router.post("/")
async def create_form(form: FormIn) -> FormOut:
    return await controller.create_form(form)


@router.put("/{form_id}")
async def update_form(form_id: uuid.UUID, form: FormIn) -> FormOut:
    try:
        return await controller.update_form(form_id, form)
    except FormNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{form_id}/questions")
async def get_form_questions(form_id: uuid.UUID) -> list[QuestionOut]:
    return await controller.get_form_questions(form_id)


@router.post("/{form_id}/questions")
async def create_question(form_id: uuid.UUID, question: QuestionIn) -> QuestionOut:
    return await controller.create_question(form_id, question)


@router.get("/{form_id}/questions/{question_id}")
async def get_question(question_id: uuid.UUID) -> QuestionOut:
    try:
        return await controller.get_question(question_id)
    except QuestionNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{form_id}/questions/{question_id}")
async def update_question(question_id: uuid.UUID, question: QuestionIn) -> QuestionOut:
    try:
        return await controller.update_question(question_id, question)
    except QuestionNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
