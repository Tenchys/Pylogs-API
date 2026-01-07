from fastapi import APIRouter, Depends, Request
from newLog.Servicio import newlogsService, newlogmodels
from sqlalchemy.orm import Session
from config.database import get_db


newlogRouter = APIRouter()
rutaBase = "/newlogs"

@newlogRouter.post(f"{rutaBase}/crear", response_model=newlogmodels.logsInfoLogResponse)
async def createLogs(log: newlogmodels.logCreate,db: Session = Depends(get_db)):
    try:
        newlog =  await newlogsService.addLog(db, log)
        return newlog
    except Exception as e:
        return str(e)
    
