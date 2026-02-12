from typing import Optional, Any
from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid

from src.Cliente.Servicio import ClienteModel
from src.Cliente.Infra import ClientesInfra


async def add_clienteService(db: Session, cliente: ClienteModel.clienteNew) -> ClienteModel.clienteResponse:

    strUuid = str(uuid.uuid4())
    newcliente = ClientesInfra.add_clientes(db, cliente.nombre, strUuid, cliente.vigencia)
    return newcliente


async def add_aplicacionService(db: Session, aplicacion: ClienteModel.aplicacionNew):
    uncliente = ClientesInfra.get_cliente(db, aplicacion.cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    strUuid = str(uuid.uuid4())
    newApp = ClientesInfra.add_aplicacion(db, nombre=aplicacion.nombre, uuid=strUuid, vigencia=aplicacion.vigencia, cliente_uuid=aplicacion.cliente_uuid)
    return newApp


async def get_clienteService(db: Session, cliente_uuid: str):
    uncliente = ClientesInfra.get_cliente(db, cliente_uuid=cliente_uuid)
    if uncliente is None:
        raise HTTPException(status_code=404)
    return uncliente

async def del_clienteService(db: Session, cliente_uuid: str):
    ClientesInfra.del_cliente(db=db, cliente_uuid=cliente_uuid)
    result = ClienteModel.ServiceResponseBase(mensaje="Cliente Eliminado")
    return result

async def udp_ClienteService(db: Session, clienteRequest: ClienteModel.updClienteRequest):
    unCliente = ClientesInfra.upd_Cliente(db=db, cliente_uuid=clienteRequest.uuid, vigencia=clienteRequest.vigencia, nombre=clienteRequest.nombre)
    return unCliente

async def get_aplicacion(db: Session, aplicacion_uuid: str):
    appObj = ClientesInfra.get_aplicacion(db, aplicacion_uuid=aplicacion_uuid)
    return appObj

async def get_aplicacion_with_cliente(db: Session, aplicacion_uuid: str) -> Optional[Any]:
    """Obtiene una aplicación junto con su cliente relacionado"""
    appObj = ClientesInfra.get_aplicacion_with_cliente(db, aplicacion_uuid=aplicacion_uuid)
    return appObj