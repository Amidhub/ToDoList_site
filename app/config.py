from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DB_HOST : str
    DB_PORT : int
    DB_USER : str
    DB_PASS : str
    DB_NAME : str
    ALGORITM : str
    SIGN : str
    class Config:
        env_file = ".env"
        
setting = Setting()