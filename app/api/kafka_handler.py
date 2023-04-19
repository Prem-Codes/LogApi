from app.api.models.log_entry import LogEntry
from app.api.log_handler_factory import LogHandler


class KafkaHandler(LogHandler):
    def __init__(self, topic):
        # Initialize Kafka producer here
        pass

    def write(self, log_entry: LogEntry):
        # Write log
        # Convert log_entry to JSON format
        log_json = log_entry.json()
        # Send log to Kafka topic
        # kafka_producer.send(topic, log_json)
        print(f"Sent log to Kafka: {log_json}")
