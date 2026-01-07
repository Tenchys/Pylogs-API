from http.client import HTTPException
from logCliente.Infra.logClientesInfra import get_clientes, add_clientes, get_cliente, add_aplicacion, del_cliente, upd_Cliente 
from sqlalchemy.orm import Session
from logCliente.Servicio.Model.logClienteModel import ServiceResponseBase, clienteBase, clienteNew, clienteResponse, aplicacionNew, updClienteRequest
import uuid


async def add_clienteService(db: Session, cliente: clienteNew):

    strUuid = str(uuid.uuid4())
    newcliente = add_clientes(db, cliente.nombre, strUuid, cliente.vigencia)
    return newcliente


async def add_aplicacionService(db: Session, aplicacion: aplicacionNew):
    uncliente = get_cliente(db, aplicacion.cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    strUuid = str(uuid.uuid4())
    newApp = add_aplicacion(db, nombre=aplicacion.nombre, uuid=strUuid, vigencia=aplicacion.vigencia, cliente_uuid=aplicacion.cliente_uuid)
    return newApp


async def get_clienteService(db: Session, cliente_uuid: str):
    uncliente = get_cliente(db, cliente_uuid=cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    return uncliente

async def del_clienteService(db: Session, cliente_uuid: str):
    del_cliente(db=db, cliente_uuid=cliente_uuid)
    result = ServiceResponseBase(mensaje="Cliente Eliminado")
    return result

async def udp_ClienteService(db: Session, clienteRequest: updClienteRequest):
    unCliente = upd_Cliente(db=db, cliente_uuid=clienteRequest.uuid, vigencia=clienteRequest.vigencia, nombre=clienteRequest.nombre)
    return unCliente