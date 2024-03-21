from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import get_settings
from app.utils import VerifyToken

app = FastAPI()
auth = VerifyToken()
settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.local_origin, settings.deployed_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
