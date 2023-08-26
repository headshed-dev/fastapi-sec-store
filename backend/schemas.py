from datetime import datetime
from typing import List
from pydantic import BaseModel
import uuid

class AnswerBaseSchema(BaseModel):
    id: uuid.UUID  
    name: str
    color: str
    quest: str
    swift_air_speed: int
    may_pass: bool
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed  = True