from fastapi import APIRouter, Depends, Request
from src.log.Servicio import logService, logmodels
from sqlalchemy.orm import Session
from src.config.database import get_db


route = APIRouter()
rutaBase = "/logs"

@route.post(f"{rutaBase}/crear", response_model=logmodels.logsInfoLogResponse)
async def createLogs(log: logmodels.logCreate,db: Session = Depends(get_db)):
    try:
        newlog =  await logService.addLog(db, log)
        return newlog
    except Exception as e:
        return str(e)
    
