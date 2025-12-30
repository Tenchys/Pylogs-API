from fastapi import FastAPI
from health.healthRoute import route as healthRoute
from newLog.Router.newLogRouter import newlogRouter
from logCliente.Router.logClienteRouter import logClienteRouter

from newLog.Infra.Entities import logsEntities
from logCliente.Infra.Entities import logClientesEntity
from config.database import engine

def routes(app: FastAPI):
    app.include_router(healthRoute)
    app.include_router(newlogRouter)
    app.include_router(logClienteRouter)


def loadModels():
    logsEntities.Base.metadata.create_all(bind=engine)
    logClientesEntity.Base.metadata.create_all(bind=engine)
