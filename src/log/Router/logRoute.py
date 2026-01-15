from fastapi import APIRouter, Depends, HTTPException, Request
from src.log.Servicio import logService, logmodels
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.auth.dependencies import verify_app_client

route = APIRouter()
rutaBase = "/logs"




@route.post(f"{rutaBase}/crear", response_model=logmodels.logsInfoLogResponse, dependencies=[Depends(verify_app_client)])
async def createLogs(log: logmodels.logCreate, request: Request,db: Session = Depends(get_db)):
    try:
        log.uuid = request.headers.get("x-aplicationid")
        newlog = await logService.addLog(db, log)
        return newlog
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

