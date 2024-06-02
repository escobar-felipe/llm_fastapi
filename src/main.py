import logging
import os

import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from handler_error import handle_error
from routers.chat.router import chat_router
from utils.functions import get_current_username_docs

# Create logger
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
)
logger = logging.getLogger()


app = FastAPI(
    title="TGS - API",
    description="Docs API - THERAPEUTIC GUIDELINES SMOKING",
    redoc_url=None,
    openapi_url=None,
    docs_url=None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

SECRET_KEY: str = os.environ.get("SECRET_KEY")

if SECRET_KEY is None:
    raise "Missing SECRET_KEY"


@app.get("/")
async def root():
    return {"message": "tgs api is alive"}


@app.get("/ping")
async def health():
    return {"message": "tgs api alive"}


@app.get("/docs", include_in_schema=False)
async def get_swagger_documentation(username: str = Depends(get_current_username_docs)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(username: str = Depends(get_current_username_docs)):
    return get_redoc_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(get_current_username_docs)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)


@app.exception_handler(Exception)
async def all_exceptions_handler(request: Request, error: Exception):
    return handle_error(error)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
