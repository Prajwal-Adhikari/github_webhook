from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    GITHUB_WEBHOOK_SECRET: str

    class Config:
        env_file = ".env"
    
settings = Settings()