from pydantic import BaseSettings


class AppSettings(BaseSettings):
    APP_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    return AppSettings()