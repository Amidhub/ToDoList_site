from sqlalchemy import select, insert, delete
from app.database import async_session_maker
from app.Tasks.models import Tasks

class TaskReq:
    
    model = Tasks
    
    @classmethod
    async def get_all_by_id(cls, id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id = id)
            res = await session.execute(query)
            return res.scalars().all()
    
    @classmethod
    async def get_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            res = await session.execute(query)
            return res.scalars().one_or_none()
    
    @classmethod
    async def get_one_by_id(cls,  id : int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = id)
            
            res = await session.execute(query)
            return res.scalars().one_or_none()
        
    @classmethod
    async def add_task(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            
    @classmethod
    async def delete_task(cls, **data):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**data)
            await session.execute(query)
            await session.commit()