from fastapi import APIRouter

from app.api.routes import moods, activities

api_router = APIRouter()

api_router.include_router(moods.router, prefix="/moods", tags=["moods"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
