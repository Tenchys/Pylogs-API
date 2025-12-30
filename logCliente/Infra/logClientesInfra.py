from logCliente.Infra.Entities.logClientesEntity import cliente
from sqlalchemy.orm import Session

def get_clientes(db: Session):
    clientes = db.query(cliente).all()
    return clientes

def add_clientes(db: Session, nombre: str, uuid: str, vigencia: bool):
    newCliente = cliente(nombre=nombre, uuid=uuid, vigencia=vigencia)
    db.add(newCliente)
    db.commit()
    db.refresh(newCliente)
    return newCliente
