from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import startup


startup.loadModels()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a orígenes específicos
    allow_methods=["*"],
    allow_headers=["*"],
)
startup.routes(app)


