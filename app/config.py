from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AgentOps Platform"
    APP_VERSION: str = "0.1.0"

    LLM_PROVIDER: str = "groq"
    MODEL_NAME: str = "llama-3.3-70b-versatile"

    GROQ_API_KEY: str 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",   # ignore extra env variables
    )


settings = Settings()