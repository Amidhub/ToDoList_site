from app.database import Base
from sqlalchemy import Integer, JSON, Column, String

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)