from app.api.models.log_entry import LogEntry
from app.api.kafka_handler import KafkaHandler
from app.api.file_handler import FileHandler
from app.api.mq_handler import MQHandler
from app.config.base import settings


class LogService:
    def __init__(self):
        self.kafka_handler = KafkaHandler(settings.KAFKA_TOPIC)
        self.file_handler = FileHandler(settings.LOG_FILE)
        self.mq_handler = MQHandler(settings.MQ_TOPIC)

    def log(self, log_entry: LogEntry):
        self.kafka_handler.write(log_entry)
        self.file_handler.write(log_entry)
        self.mq_handler.write(log_entry)
