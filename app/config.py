from pydantic_settings import BaseSettings
from typing import Literal

class Setting(BaseSettings):
    MODE : Literal["DEV", "TEST", "PROD"]
    
    DB_HOST : str
    DB_PORT : int
    DB_USER : str
    DB_PASS : str
    DB_NAME : str
    ALGORITM : str
    SIGN : str
    
    TEST_DB_HOST : str
    TEST_DB_PORT : int
    TEST_DB_USER : str
    TEST_DB_PASS : str
    TEST_DB_NAME : str
    class Config:
        env_file = ".env"
        
setting = Setting()