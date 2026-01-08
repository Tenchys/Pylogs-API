from fastapi import APIRouter
from . import healthModel
route = APIRouter()

rutaBase = "/health"

@route.get(f"{rutaBase}")
async def get():
    response = healthModel.HealthModel()
    return response