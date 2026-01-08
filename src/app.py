from fastapi import FastAPI
from src.config import startup


startup.loadModels()

app = FastAPI()
startup.routes(app)


