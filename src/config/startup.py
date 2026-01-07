from fastapi import FastAPI

from src.health import healthRoute
from src.log.Router import logRoute
from src.logCliente.Router import logClienteRouter

##from newLog.Infra.Entities import logsEntities
from src.log.Infra import logsEntities
from src.logCliente.Infra import logClientesEntity
from .database import engine

def routes(app: FastAPI):
    app.include_router(healthRoute.route)
    app.include_router(logRoute.route)
    app.include_router(logClienteRouter.route)


def loadModels():
    logsEntities.Base.metadata.create_all(bind=engine)
    logClientesEntity.Base.metadata.create_all(bind=engine)
