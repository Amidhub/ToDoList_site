from fastapi.testclient import TestClient
import pytest
from app.config import setting

from app.database import engine, Base, async_session_maker
from sqlalchemy import insert

import json

from app.Users.models import User
from app.Tasks.models import Tasks

from app.main import app as fastapi_app



@pytest.fixture(scope = "session", autouse=True)
async def prepare_database():
    assert setting.MODE == "TEST"
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
    def open_mock_json(model : str):
        with open(f"app/tests/mock_{model}.json", encoding='utf-8') as f:
            return json.load(f)

    users = open_mock_json('users')
    tasks = open_mock_json('tasks')
    
    
    async with async_session_maker() as session:
        add_users = insert(User).values(users)
        add_tasks = insert(Tasks).values(tasks)

        await session.execute(add_users)
        await session.execute(add_tasks)
        
        await session.commit()
        
@pytest.fixture(scope='function')
def ac():
    with TestClient(app=fastapi_app, base_url="http://testserver") as ac:
        yield ac