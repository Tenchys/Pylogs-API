from sqlalchemy.orm import Session
from newLog.Infra.Entities.logsEntities import log

def get_logs(db: Session):
    logs = db.query(log).all()
    return logs

def create_log(db: Session, mensaje: str, alerta: bool = False):
    newlog = log(mensaje=mensaje, alerta=alerta)
    db.add(newlog)
    db.commit()
    db.refresh(newlog)
    return newlog