from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.Users.router import router as user_router
from app.Tasks.router import router as task_router
from app.Users.dependencise import get_current_user
from app.Users.models import User
from app.Tasks.dao import TaskReq

app = FastAPI()

# Настройка шаблонов
templates = Jinja2Templates(directory="app/templates")

app.include_router(user_router)
app.include_router(task_router)

# 📌 НОВЫЕ ЭНДПОИНТЫ ДЛЯ HTML

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/tasks", response_class=HTMLResponse)
async def tasks_page(request: Request, user: User = Depends(get_current_user)):
    tasks = await TaskReq.get_all_by_id(id=user.id)
    return templates.TemplateResponse("tasks.html", {
        "request": request, 
        "user": user,
        "tasks": tasks
    })

@app.get("/logout")
async def logout_page():
    response = RedirectResponse(url="/login")
    response.delete_cookie("user_access_token")
    return response