from newLog.Servicio.Models.newlogmodels import logCreate
from newLog.Infra.newlogInfra import get_logs, create_log
from sqlalchemy.orm import Session


async def addLog(db: Session ,mensaje: str, alerta: bool):
    newlog = create_log(db, mensaje,alerta)
    return newlog