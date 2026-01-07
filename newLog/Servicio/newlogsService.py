from newLog.Servicio.Models.newlogmodels import logCreate, logsInfoLogResponse
from newLog.Infra import newlogInfra
from sqlalchemy.orm import Session


async def addLog(db: Session, log: logCreate) -> logsInfoLogResponse:
    newlog = newlogInfra.create_log(db, log)
    return newlog