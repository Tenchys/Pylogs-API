from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config.database import get_db

from src.Cliente.Servicio import ClienteModel, ClienteServicio


route = APIRouter()

rutaBase = f"/cliente"



@route.post(f"{rutaBase}/crear")
async def crear_cliente(cliente: ClienteModel.clienteNew, db: Session = Depends(get_db)):
    try:
        new_cliente = await ClienteServicio.add_clienteService(db, cliente)
        return new_cliente
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@route.post(f"{rutaBase}/crearAplicacion")
async def crear_aplicacion(aplicacion: ClienteModel.aplicacionNew, db: Session = Depends(get_db)):
    try:
        new_aplicacion = await ClienteServicio.add_aplicacionService(db=db, aplicacion=aplicacion)
        return new_aplicacion
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@route.get(f"{rutaBase}/obtener", response_model=ClienteModel.clienteResponse)
async def getCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await ClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@route.get(f"{rutaBase}/obtenerAplicaciones", response_model=ClienteModel.clienteAppResponse)
async def getCLienteAPP(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await ClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@route.delete(f"{rutaBase}/borrar", response_model=ClienteModel.ServiceResponseBase)
async def delCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        result = await ClienteServicio.del_clienteService(db=db, cliente_uuid=cliente_uuid)
        return result
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@route.patch(f"{rutaBase}/vigencia", response_model=ClienteModel.clienteResponse)
async def updVigencia(clienteRequest: ClienteModel.updClienteRequest, db: Session = Depends(get_db)):
    try:
        unCliente = await ClienteServicio.udp_ClienteService(db=db, clienteRequest=clienteRequest)
        return unCliente
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")