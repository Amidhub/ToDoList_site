'''from fastapi import APIRouter, HTTPException, Request, Response, status, Depends
from app.Tasks.Schemas import taskS
from app.Tasks.dao import TaskReq
from app.Users.models import User
from app.Users.dependencise import get_current_user

router = APIRouter(
    prefix="/task",
    tags=["Работа с тасками"]
)


@router.get('/get/{user_id}')
async def get(user_id : int, user : User = Depends(get_current_user)):
    return await TaskReq.get_all_by_id(id = user_id)


from fastapi.responses import RedirectResponse

@router.post('/add')
async def add(task: taskS, user: User = Depends(get_current_user)):
    await TaskReq.add_task(title=task.title, description=task.description, user_id=user.id)
    return RedirectResponse(url="/tasks", status_code=303)

@router.post('/delete/{id}')
async def delete(id: int, user: User = Depends(get_current_user)):
    await TaskReq.delete_task(id=id)
    return RedirectResponse(url="/tasks", status_code=303)
'''
from fastapi import APIRouter, HTTPException, Request, Response, status, Depends, Form
from fastapi.responses import RedirectResponse
from app.Tasks.dao import TaskReq
from app.Users.models import User
from app.Users.dependencise import get_current_user

router = APIRouter(
    prefix="/task",
    tags=["Работа с тасками"]
)

@router.get('/get/{user_id}')
async def get(user_id: int, user: User = Depends(get_current_user)):
    return await TaskReq.get_all_by_id(id=user_id)

@router.post('/add')
async def add(
    title: str = Form(...),
    description: str = Form(None),
    user_id: int = Form(...),
    user: User = Depends(get_current_user)
):
    await TaskReq.add_task(title=title, description=description, user_id=user_id)
    return RedirectResponse(url="/tasks", status_code=303)

@router.post('/delete/{id}')
async def delete(id: int, user: User = Depends(get_current_user)):
    await TaskReq.delete_task(id=id)
    return RedirectResponse(url="/tasks", status_code=303)