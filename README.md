# ToDoList_site на FastAPI

Веб-приложение для управления задачами с авторизацией и адаптивным интерфейсом.
Проект включает полное покрытие тестами API-эндпоинтов и бизнес-логики с использованием pytest и асинхронных фикстур.

## Технологии

**Backend:**
- FastAPI
- SQLAlchemy + Alembic  
- JWT аутентификация
- PostgreSQL

**Frontend:**
- Jinja2 шаблоны
- CSS
- HTML5

**Тестирование:**
- pytest
- pytest-asyncio
- httpx

## Установка и запуск

**Клонирование и настройка**
```bash
git clone https://github.com/Amidhub/ToDoList_site.git
cd ToDoList_site
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```


Создайте .env файл:

env
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASS=your_password
DB_NAME=todo_app
ALGORITM=HS256
SIGN=your_secret_key
```

Запуск

```bash
alembic upgrade head
uvicorn app.main:app --reload
```
Приложение доступно по адресу: http://localhost:8000


Структура проекта
```
ToDoList_FastAPI/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── conftest.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── tasks.html
│   ├── Users/
│   │   ├── router.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── auth.py
│   │   ├── dao.py
│   │   └── dependencise.py
│   ├── Tasks/
│   │   ├── router.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── dao.py
│   ├── tests/
│   │   ├── unit_tests/test_api.py
│   │   ├── conftest.py
│   │   ├── mock_tasks.json
│   │   └── mock_users.json
├── migrations/
│   ├── env.py
│   ├── versions/
│   └── script.py.mako
├── requirements.txt
├── alembic.ini
├── pytest.ini
└── README.md
```
