from abc import ABC, abstractmethod

from app.api.models.log_entry import LogEntry


class LogHandler(ABC):
    @abstractmethod
    def write(self, log_entry: LogEntry):
        pass
