from app.api.models.log_entry import LogEntry
from app.api.log_handler_factory import LogHandler


class MQHandler(LogHandler):
    def __init__(self, topic):
        # Initialize MQ producer here
        pass

    def write(self, log_entry: LogEntry):
        # Write log to MQ topic
        # Convert log_entry to JSON format
        log_json = log_entry.json()
        # Send log to MQ topic
        # mq_producer.send(topic, log_json)
        print(f"Sent log to MQ: {log_json}")
