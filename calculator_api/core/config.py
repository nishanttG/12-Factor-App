from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Calculator API"

    class Config:
        env_file = ".env"

settings = Settings()
