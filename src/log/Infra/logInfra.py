from typing import List
from sqlalchemy.orm import Session
from .Entities import logsEntities
from src.log.Servicio import logmodels

def get_logs(db: Session):
    logs = db.query(logsEntities.log).all()
    return logs

def create_log(db: Session, log_data: logmodels.logCreate):
    newlog = logsEntities.log(mensaje=log_data.mensaje, alerta=log_data.alerta, app_uuid=log_data.uuid)
    if log_data.infologs is not None:
        for info in log_data.infologs:
            newlog.infologs.append(logsEntities.infolog(nombre_alerta=info.nombre_alerta, valor_alerta=info.valor_alerta))
    db.add(newlog)
    db.commit()
    db.refresh(newlog)
    return newlog



                