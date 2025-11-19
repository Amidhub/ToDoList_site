'''from fastapi import APIRouter, HTTPException, Request, Response, status
from app.Users.Schemas import authS
from app.Users.auth import get_password_hash
from app.Users.dao import UserReq
from app.Users.auth import login_user, create_access_token
from fastapi.responses import RedirectResponse


router = APIRouter(
    prefix="/auth",
    tags=["Регистрация/авторизация"]
)


@router.post('/login')
async def login_users(response: Response, user_data: authS):
    user = await login_user(user_data.name, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    jwt_token = create_access_token({'sub': str(user.id)})
    response = RedirectResponse(url="/tasks", status_code=303)
    response.set_cookie('user_access_token', jwt_token, httponly=True)
    return response

@router.post('/register')
async def register_user(user_data: authS):
    existing_user = await UserReq.get_one_or_none(name=user_data.name)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой ник занят")
    
    hashed_password = get_password_hash(user_data.password)
    await UserReq.add(name=user_data.name, hashed_password=hashed_password)
    
    return RedirectResponse(url="/login", status_code=303)

@router.post('/logout')
async def login_users(response : Response) -> None:
    response.delete_cookie('user_access_token')

'''
from fastapi import APIRouter, HTTPException, Request, Response, status, Form
from fastapi.responses import RedirectResponse
from app.Users.auth import get_password_hash, login_user, create_access_token
from app.Users.dao import UserReq

router = APIRouter(
    prefix="/auth",
    tags=["Регистрация/авторизация"]
)

@router.post('/register')
async def register_user(
    name: str = Form(...),
    password: str = Form(...)
):
    existing_user = await UserReq.get_one_or_none(name=name)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Такой ник занят")
    
    hashed_password = get_password_hash(password)
    await UserReq.add(name=name, hashed_password=hashed_password)
    return RedirectResponse(url="/login", status_code=303)

@router.post('/login')
async def login_users(
    response: Response,
    name: str = Form(...),
    password: str = Form(...)
):
    user = await login_user(name, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    jwt_token = create_access_token({'sub': str(user.id)})
    response = RedirectResponse(url="/tasks", status_code=303)
    response.set_cookie('user_access_token', jwt_token, httponly=True)
    return response

@router.post('/logout')
async def logout_users(response: Response):
    response = RedirectResponse(url="/login")
    response.delete_cookie('user_access_token')
    return response