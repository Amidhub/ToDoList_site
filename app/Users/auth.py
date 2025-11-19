import jwt 
from datetime import timedelta, datetime
from passlib.context import CryptContext

from app.Users.dao import UserReq
from app.config import setting


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data : dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({'exp' : expire })
    encoded_jwt = jwt.encode(
        to_encode, setting.SIGN, setting.ALGORITM
    )
    return encoded_jwt


'''def login_user(name : str, password : str):
    user = UserReq.get_one_or_none(name = name)
    if not user and not verify_password(password, user.password):
        return None
    return user
'''
async def login_user(name: str, password: str):
    user = await UserReq.get_one_or_none(name=name)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user