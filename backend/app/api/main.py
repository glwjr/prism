from fastapi import APIRouter

from app.api.routes import moods

api_router = APIRouter()
api_router.include_router(moods.router, prefix="/moods", tags=["moods"])
