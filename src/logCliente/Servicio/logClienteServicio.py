from http.client import HTTPException
from sqlalchemy.orm import Session
import uuid

from src.logCliente.Servicio import logClienteModel
from src.logCliente.Infra import logClientesInfra


async def add_clienteService(db: Session, cliente: logClienteModel.clienteNew):

    strUuid = str(uuid.uuid4())
    newcliente = logClientesInfra.add_clientes(db, cliente.nombre, strUuid, cliente.vigencia)
    return newcliente


async def add_aplicacionService(db: Session, aplicacion: logClienteModel.aplicacionNew):
    uncliente = logClientesInfra.get_cliente(db, aplicacion.cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    strUuid = str(uuid.uuid4())
    newApp = logClientesInfra.add_aplicacion(db, nombre=aplicacion.nombre, uuid=strUuid, vigencia=aplicacion.vigencia, cliente_uuid=aplicacion.cliente_uuid)
    return newApp


async def get_clienteService(db: Session, cliente_uuid: str):
    uncliente = logClientesInfra.get_cliente(db, cliente_uuid=cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    return uncliente

async def del_clienteService(db: Session, cliente_uuid: str):
    logClientesInfra.del_cliente(db=db, cliente_uuid=cliente_uuid)
    result = logClienteModel.ServiceResponseBase(mensaje="Cliente Eliminado")
    return result

async def udp_ClienteService(db: Session, clienteRequest: logClienteModel.updClienteRequest):
    unCliente = logClientesInfra.upd_Cliente(db=db, cliente_uuid=clienteRequest.uuid, vigencia=clienteRequest.vigencia, nombre=clienteRequest.nombre)
    return unCliente