from fastapi import APIRouter, Depends, HTTPException, Request
from src.log.Servicio import logService, logmodels
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.Cliente.Servicio import ClienteServicio, ClienteModel

route = APIRouter()
rutaBase = "/logs"


async def verificar_vigencia_Permisos(request: Request, db: Session = Depends(get_db)):
    try:
        await logService.middleware_verifica_appcliente(db, request)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))

@route.post(f"{rutaBase}/crear", response_model=logmodels.logsInfoLogResponse, dependencies=[Depends(verificar_vigencia_Permisos)])
async def createLogs(log: logmodels.logCreate, request: Request,db: Session = Depends(get_db)):
    try:
        log.uuid = request.headers.get("x-aplicationid")
        newlog = await logService.addLog(db, log)
        return newlog
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

