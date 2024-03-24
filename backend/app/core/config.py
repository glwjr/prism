from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str
    local_origin: str
    deployed_origin: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
