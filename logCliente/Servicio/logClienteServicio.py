from logCliente.Infra.logClientesInfra import get_clientes, add_clientes
from sqlalchemy.orm import Session
from logCliente.Servicio.Model.logClienteModel import clienteBase, clienteNew, clienteResponse
import uuid


async def add_clienteService(db: Session, cliente: clienteNew):

    strUuid = str(uuid.uuid4())
    newcliente = add_clientes(db, cliente.nombre, strUuid, cliente.vigencia)
    return newcliente