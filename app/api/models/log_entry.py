from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class LogEntry(BaseModel):
    application_id: str
    trace_id: Optional[str] = None
    severity: str
    timestamp: Optional[datetime] = None
    message: str
    component_name: Optional[str] = None
    request_id: Optional[str] = None

    @validator('timestamp', pre=True, always=True)
    def set_timestamp(cls, v):
        return v or datetime.utcnow()
