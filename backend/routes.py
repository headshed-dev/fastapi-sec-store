
from fastapi import status as STATUS, HTTPException, APIRouter


from pydantic import BaseModel
from typing import List
from schemas import AnswerBaseSchema, AnswerSchema
from database import SessionLocal
import models

router = APIRouter(
    prefix="/api/v1",
    tags=["API v1"],
)

db = SessionLocal()

@router.get("/healthchecker")
def health():
    return {"message": "Welcome to fastapi-sec-store with Headshed"}

@router.get('/answers', 
    response_model=List[AnswerSchema],
    status_code=200)
async def get_all_answers():
    answers = db.query(models.Answer).all() 
    return answers

@router.post('/answers',
    response_model=AnswerBaseSchema,
    status_code=STATUS.HTTP_201_CREATED)
async def create_answer(answer: AnswerBaseSchema):
    db_answer = models.Answer(**answer.dict())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

@router.put('/answers/{answer_id}',
    response_model=AnswerBaseSchema,
    status_code=STATUS.HTTP_200_OK)
async def update_answer(answer_id: int, answer: AnswerBaseSchema):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not db_answer:
        raise HTTPException(status_code=STATUS.HTTP_404_NOT_FOUND, detail="Answer not found")
    # db_answer.answer = answer.answer
    db_answer.name = answer.name
    db_answer.color = answer.color
    db_answer.quest = answer.quest
    db_answer.swift_air_speed = answer.swift_air_speed
    db_answer.may_pass = answer.may_pass
    db.commit()
    db.refresh(db_answer)
    return db_answer

@router.delete('/answers/{answer_id}',
    status_code=STATUS.HTTP_204_NO_CONTENT)
async def delete_answer(answer_id: int):
    db_answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not db_answer:
        raise HTTPException(status_code=STATUS.HTTP_404_NOT_FOUND, detail="Answer not found")
    db.delete(db_answer)
    db.commit()
    return {"message": "Answer deleted successfully"}