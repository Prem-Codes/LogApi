from .base import Settings


class DevelopmentSettings(Settings):
    kafka_bootstrap_servers = "localhost:9092"


settings = DevelopmentSettings()
