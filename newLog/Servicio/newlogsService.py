from newLog.Servicio.Models.newlogmodels import logCreate, logsInfoLogResponse
from newLog.Infra.newlogInfra import get_logs, create_log
from sqlalchemy.orm import Session


async def addLog(db: Session, log: logCreate) -> logsInfoLogResponse:
    newlog = create_log(db, log)
    return newlog