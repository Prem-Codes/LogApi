from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    kafka_bootstrap_servers: Optional[str]
    kafka_topic: Optional[str]
    log_file: Optional[str]

    class Config:
        env_prefix = "LOG_"
        case_sensitive = True


settings = Settings()
