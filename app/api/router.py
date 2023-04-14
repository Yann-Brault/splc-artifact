from fastapi import APIRouter

from .models import Configuration
from app.generator.generate import generate_nb

configurator_router = APIRouter()


@ configurator_router.post("/generate")
async def generate(payload: Configuration):
    generate_nb(payload.config)
    return {"message": "Hello World"}
