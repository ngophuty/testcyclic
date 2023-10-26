from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    HOST: Optional[str]
    PORT: Optional[int]
    MAIN_SOURCE: str = "main:app"



settings = Settings()
    