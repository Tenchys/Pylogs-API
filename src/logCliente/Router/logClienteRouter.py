from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db

from src.logCliente.Servicio import logClienteModel
from src.logCliente.Servicio import logClienteServicio


route = APIRouter()

rutaBase = f"/cliente"



@route.post(f"{rutaBase}/crear")
async def crear_cliente(cliente: logClienteModel.clienteNew, db: Session = Depends(get_db)):
    try:
        new_cliente = await logClienteServicio.add_clienteService(db, cliente)
        return new_cliente
    except Exception as e:
        return str(e)
    
@route.post(f"{rutaBase}/crearAplicacion")
async def crear_aplicacion(aplicacion: logClienteModel.aplicacionNew, db: Session = Depends(get_db)):
    try:
        new_aplicacion = await logClienteServicio.add_aplicacionService(db=db, aplicacion=aplicacion)
        return new_aplicacion
    except Exception as e:
        return str(e)
    
@route.get(f"{rutaBase}/obtener", response_model=logClienteModel.clienteResponse)
async def getCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await logClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except Exception as e:
        return str(e)

@route.get(f"{rutaBase}/obtenerAplicaciones", response_model=logClienteModel.clienteAppResponse)
async def getCLienteAPP(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await logClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except Exception as e:
        return str(e)
    
@route.delete(f"{rutaBase}/borrar", response_model=logClienteModel.ServiceResponseBase)
async def delCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        result = await logClienteServicio.del_clienteService(db=db, cliente_uuid=cliente_uuid)
        return result
    except Exception as e:
        return str(e)
    
@route.patch(f"{rutaBase}/vigencia", response_model=logClienteModel.clienteResponse)
async def updVigencia(clienteRequest: logClienteModel.updClienteRequest, db: Session = Depends(get_db)):
    try:
        unCliente = await logClienteServicio.udp_ClienteService(db=db, clienteRequest=clienteRequest)
        return unCliente
    except Exception as e:
        return str(e)  