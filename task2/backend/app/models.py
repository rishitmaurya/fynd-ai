# models.py
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .db import Base

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=False)
    ai_reply = Column(Text, nullable=True)
    ai_summary = Column(Text, nullable=True)
    ai_actions = Column(Text, nullable=True)
