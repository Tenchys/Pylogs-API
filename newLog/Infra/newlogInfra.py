from typing import List
from sqlalchemy.orm import Session
from newLog.Infra.Entities.logsEntities import log, infolog
from newLog.Servicio.Models.newlogmodels import infologBase, infologResponse, logCreate, logsInfoLogResponse

def get_logs(db: Session):
    logs = db.query(log).all()
    return logs

def create_log(db: Session, log_data: logCreate):
    newlog = log(mensaje=log_data.mensaje, alerta=log_data.alerta)
    for info in log_data.infologs:
        newlog.infologs.append(infolog(nombre_alerta=info.nombre_alerta, valor_alerta=info.valor_alerta))
    db.add(newlog)
    db.commit()
    db.refresh(newlog)


    return newlog



                