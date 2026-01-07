from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from logCliente.Servicio.Model.logClienteModel import ServiceResponseBase, clienteNew, aplicacionNew, clienteResponse, clienteAppResponse, updClienteRequest
from logCliente.Servicio.logClienteServicio import add_clienteService, add_aplicacionService, del_clienteService, get_clienteService, udp_ClienteService

logClienteRouter = APIRouter()

rutaBase = f"/cliente"



@logClienteRouter.post(f"{rutaBase}/crear")
async def crear_cliente(cliente: clienteNew, db: Session = Depends(get_db)):
    try:
        new_cliente = await add_clienteService(db, cliente)
        return new_cliente
    except Exception as e:
        return str(e)
    
@logClienteRouter.post(f"{rutaBase}/crearAplicacion")
async def crear_aplicacion(aplicacion: aplicacionNew, db: Session = Depends(get_db)):
    try:
        new_aplicacion = await add_aplicacionService(db=db, aplicacion=aplicacion)
        return new_aplicacion
    except Exception as e:
        return str(e)
    
@logClienteRouter.get(f"{rutaBase}/obtener", response_model=clienteResponse)
async def getCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except Exception as e:
        return str(e)

@logClienteRouter.get(f"{rutaBase}/obtenerAplicaciones", response_model=clienteAppResponse)
async def getCLienteAPP(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        unCliente = await get_clienteService(db, cliente_uuid=cliente_uuid)
        return unCliente
    except Exception as e:
        return str(e)
    
@logClienteRouter.delete(f"{rutaBase}/borrar", response_model=ServiceResponseBase)
async def delCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    try:
        result = await del_clienteService(db=db, cliente_uuid=cliente_uuid)
        return result
    except Exception as e:
        return str(e)
    
@logClienteRouter.patch(f"{rutaBase}/vigencia", response_model=clienteResponse)
async def updVigencia(clienteRequest: updClienteRequest, db: Session = Depends(get_db)):
    try:
        unCliente = await udp_ClienteService(db=db, clienteRequest=clienteRequest)
        return unCliente
    except Exception as e:
        return str(e)  