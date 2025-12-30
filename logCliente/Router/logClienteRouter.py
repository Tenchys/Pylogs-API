from fastapi import APIRouter, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from logCliente.Servicio.Model.logClienteModel import clienteNew
from logCliente.Servicio.logClienteServicio import add_clienteService

logClienteRouter = APIRouter()

rutaBase = f"/cliente"

@logClienteRouter.post(f"{rutaBase}/crear")
async def crear_cliente(cliente: clienteNew, db: Session = Depends(get_db)):
    try:
        new_cliente = await add_clienteService(db, cliente)
        return new_cliente
    except Exception as e:
        return str(e)