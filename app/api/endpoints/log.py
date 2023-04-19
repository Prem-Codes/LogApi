from fastapi import APIRouter, Depends

from app.api.models.log_entry import LogEntry
from app.api.services.log_service import LogService


router = APIRouter()


@router.post("/log")
async def log(log_entry: LogEntry, log_service: LogService = Depends()):
    log_service.log(log_entry)
    return {"message": "Log entry created"}
