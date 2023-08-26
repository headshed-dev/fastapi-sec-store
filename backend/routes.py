
from fastapi import status as STATUS, HTTPException, APIRouter


from pydantic import BaseModel
from typing import List
from schemas import AnswerBaseSchema
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
    response_model=List[AnswerBaseSchema],
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