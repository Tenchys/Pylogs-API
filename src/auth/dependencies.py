from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
import hmac
import os
from src.config.database import get_db

from src.Cliente.Infra.Entities import ClientesEntity


async def verify_app_client(request: Request, db: Session = Depends(get_db)) -> None:
    """
    Dependencia de autenticación que verifica:
    1. Headers x-aplicationid y x-aplicationkey presentes
    2. API key válida (comparación segura con hmac)
    3. Aplicación existente y vigente
    4. Cliente existente y vigente
    
    Lanza HTTPException 403 si alguna verificación falla.
    """
    # Verificar headers
    appuuid_header = request.headers.get("x-aplicationid")
    appkey_header = request.headers.get("x-aplicationkey")
    if appuuid_header is None or appkey_header is None:
        raise HTTPException(status_code=403, detail="Missing authentication headers")
    
    appuuid = appuuid_header
    appkey = appkey_header
    
    # Verificar API key
    appkeystored = os.getenv("APPKEY")
    if appkeystored is None:
        raise HTTPException(status_code=500, detail="Server misconfigured")
    if not hmac.compare_digest(appkey.encode(), appkeystored.encode()):
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    # Consulta única con join para aplicación y cliente
    app_obj = db.query(ClientesEntity.aplicacion).options(
        joinedload(ClientesEntity.aplicacion.cliente)
    ).filter(ClientesEntity.aplicacion.uuid == appuuid).first()
    
    if app_obj is None:
        raise HTTPException(status_code=403, detail="Application not found")
    if not app_obj.vigencia:
        raise HTTPException(status_code=403, detail="Application inactive")
    
    cliente_obj = app_obj.cliente
    if cliente_obj is None:
        raise HTTPException(status_code=403, detail="Client not found")
    if not cliente_obj.vigencia:
        raise HTTPException(status_code=403, detail="Client inactive")
    
    # Autenticación exitosa, no retorna nada (solo pasa)
    return None