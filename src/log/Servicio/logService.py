from fastapi import Request
from sqlalchemy.orm import Session

from .Models import logmodels
from src.log.Infra import logInfra
from src.Cliente.Servicio import ClienteServicio
from src.config.getenv import get_env



async def addLog(db: Session, log: logmodels.logCreate) -> logmodels.logsInfoLogResponse:
    newlog = logInfra.create_log(db, log)
    return newlog


async def middleware_verifica_appcliente(db: Session, request: Request):
    if request.headers.get("x-aplicationid") is None or request.headers.get("x-aplicationkey") is None:
        raise PermissionError("no auth")
    appuuid = request.headers.get("x-aplicationid")
    appkey = request.headers.get("x-aplicationkey")
    appkeystored = get_env("APPKEY")
    if appkey != appkeystored:
        raise PermissionError("no appAuth")
    appObj = await ClienteServicio.get_aplicacion(db=db, aplicacion_uuid=appuuid)
    if appObj is None:
        raise PermissionError("no app")
    if appObj.vigencia == False:
        raise PermissionError("no app")
    clienteObj = await ClienteServicio.get_clienteService(db=db, cliente_uuid=appObj.cliente_uuid)
    if clienteObj is None:
        raise PermissionError("no user")
    if clienteObj.vigencia == False:
        raise PermissionError("no user")
    
