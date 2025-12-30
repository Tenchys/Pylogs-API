from fastapi import APIRouter, Depends, Request
from newLog.Servicio.Models.newlogmodels import logCreate
from newLog.Servicio import newlogsService
from sqlalchemy.orm import Session
from config.database import get_db


newlogRouter = APIRouter()
rutaBase = "/newlogs"

@newlogRouter.post(f"{rutaBase}/crear")
async def createLogs(log: logCreate, request: Request,db: Session = Depends(get_db)):
    try:
        ##newlog =  await newlogsService.addLog(db, log.mensaje, log.alerta)
        return str(request.headers.getlist)
    except Exception as e:
        return str(e)
    