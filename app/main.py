import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from app.api.endpoints import log
from app.config.base import Settings

app = FastAPI(title="My Logging System", version="0.1")

# Mounting the routers
app.include_router(log.router, prefix="/log")

# Custom JSON response handler
@app.exception_handler(Exception)
async def custom_exception_handler(request, exc):
    return JSONResponse(content={"message": str(exc)}, status_code=500)

# Swagger documentation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My Logging System",
        version="0.1",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

