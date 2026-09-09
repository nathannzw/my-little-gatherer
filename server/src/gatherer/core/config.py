from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    llm_url: str
    model_name: str

    class Config:
        env_file = ".env"


settings = Settings()