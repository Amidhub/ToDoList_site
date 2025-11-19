from pydantic import BaseModel

class authS(BaseModel):
    name : str
    password: str