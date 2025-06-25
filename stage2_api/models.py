from sqlalchemy import Column, Integer, String
from .db import Base

class PromptResult(Base):
    __tablename__ = "prompt_results"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, nullable=False)
    nike = Column(Integer, default=0)
    adidas = Column(Integer, default=0)
    hoka = Column(Integer, default=0)
    new_balance = Column(Integer, default=0)
    jordan = Column(Integer, default=0)