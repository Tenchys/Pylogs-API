from .Models import logmodels
from src.log.Infra import logInfra
from sqlalchemy.orm import Session


async def addLog(db: Session, log: logmodels.logCreate) -> logmodels.logsInfoLogResponse:
    newlog = logInfra.create_log(db, log)
    return newlog