from pydantic import BaseModel

class taskS(BaseModel):
    title : str
    description : str | None
    user_id : int