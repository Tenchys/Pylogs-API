from fastapi import FastAPI

from src.health import healthRoute
from src.log.Router import logRoute
from src.Cliente.Router import ClienteRouter


from src.log.Infra import logsEntities
from src.Cliente.Infra import ClientesEntity
from .database import engine

def routes(app: FastAPI):
    app.include_router(healthRoute.route)
    app.include_router(logRoute.route)
    app.include_router(ClienteRouter.route)


def loadModels():
    logsEntities.Base.metadata.create_all(bind=engine)
    ClientesEntity.Base.metadata.create_all(bind=engine)
