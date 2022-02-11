from fastapi import APIRouter

from app.controllers import sample

api_router = APIRouter()

# Include all controller's routers here
api_router.include_router(sample.router)
