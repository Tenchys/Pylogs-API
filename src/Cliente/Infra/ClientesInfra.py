from typing import Optional
from .Entities import ClientesEntity
from sqlalchemy.orm import Session

def get_clientes(db: Session):
    clientes = db.query(ClientesEntity.cliente).all()
    return clientes

def add_clientes(db: Session, nombre: str, uuid: str, vigencia: bool):
    newCliente = ClientesEntity.cliente(nombre=nombre, uuid=uuid, vigencia=vigencia)
    db.add(newCliente)
    db.commit()
    db.refresh(newCliente)
    return newCliente

def add_aplicacion(db: Session, nombre: str, uuid: str, vigencia: bool, cliente_uuid: str):
    newApp = ClientesEntity.aplicacion(nombre=nombre, uuid=uuid, vigencia=vigencia, cliente_uuid=cliente_uuid)
    db.add(newApp)
    db.commit()
    db.refresh(newApp)
    return newApp

def get_cliente(db: Session, cliente_uuid: str):
    unCliente = db.query(ClientesEntity.cliente).filter(ClientesEntity.cliente.uuid == cliente_uuid).first()
    return unCliente

def del_cliente(db: Session, cliente_uuid: str):
    unCliente = db.query(ClientesEntity.cliente).filter(ClientesEntity.cliente.uuid == cliente_uuid).first()
    db.delete(unCliente)
    db.commit()

def upd_Cliente(db: Session, cliente_uuid: str, vigencia: Optional[bool] = None, nombre: Optional[str] = None):
    unCliente = db.query(ClientesEntity.cliente).filter(ClientesEntity.cliente.uuid == cliente_uuid).first()
    if unCliente is None:
        return None
    if vigencia is not None:
        unCliente.vigencia = vigencia
    if nombre is not None:
        unCliente.nombre = nombre
    db.add(unCliente)
    db.commit()
    db.refresh(unCliente)
    return unCliente

def get_aplicacion(db: Session, aplicacion_uuid: str):
    appObj = db.query(ClientesEntity.aplicacion).filter(ClientesEntity.aplicacion.uuid == aplicacion_uuid).first()
    return appObj

def get_aplicacion_with_cliente(db: Session, aplicacion_uuid: str) -> Optional[ClientesEntity.aplicacion]:
    """Obtiene una aplicación junto con su cliente relacionado usando joinedload"""
    from sqlalchemy.orm import joinedload
    appObj = db.query(ClientesEntity.aplicacion).options(
        joinedload(ClientesEntity.aplicacion.cliente)
    ).filter(ClientesEntity.aplicacion.uuid == aplicacion_uuid).first()
    return appObj
