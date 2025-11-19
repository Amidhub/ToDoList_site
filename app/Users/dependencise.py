from fastapi import Request, HTTPException, status, Depends
import jwt
from jwt import PyJWTError
from app.config import setting
from datetime import datetime
from app.Users.dao import UserReq


def get_token(request : Request):
    token = request.cookies.get('user_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

async def get_current_user(token : str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token,
            setting.SIGN,
            setting.ALGORITM
        )
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="не является jwt кодом")
    
    expair : str = payload.get("exp")
    
    if (not expair) or (int(expair) < int(datetime.utcnow().timestamp())):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="истёк expair")
    
    user_id : int = int(payload.get("sub"))
    
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="в куке не информация про id")
    
    user = await UserReq.get_one_by_id(user_id)
    
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="нет пользователя с таким id")
    
    return user