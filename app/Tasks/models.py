from app.database import Base
from sqlalchemy import Integer, JSON, Column, String, Text, Boolean, ForeignKey

class Tasks(Base):
    __tablename__ = "task"
       
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # 🔑 ВНЕШНИЙ КЛЮЧ на пользователя
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)