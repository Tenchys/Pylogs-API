from fastapi import APIRouter
from health.healthModel import HealthModel
route = APIRouter()

rutaBase = "/health"

@route.get(f"{rutaBase}")
async def get():
    response = HealthModel()
    return response