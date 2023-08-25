from database import Base
from sqlalchemy import TIMESTAMP, String, Boolean, Integer, Column, Text
from sqlalchemy.sql.expression import null
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE

class Answer(Base):
    __tablename__='form_answers'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    quest = Column(String(255), nullable=False)
    swift_air_speed = Column(Integer, nullable=False)
    may_pass = Column(Boolean, default=False)
    # createdAt = Column(TIMESTAMP(timezone=True),
    #     nullable=False, server_default=func.now())
    # updatedAt = Column(TIMESTAMP(timezone=True),
    #     default=None, onupdate=func.now())
    def __repr__(self):
        return f"<Task title={self.title} status={self.status}>"