from app.api.models.log_entry import LogEntry
from app.api.log_handler_factory import LogHandler


class FileHandler(LogHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, log_entry: LogEntry):
        # Write log to file
        with open(self.file_path, "a") as f:
            f.write(log_entry.json())
            f.write("\n")