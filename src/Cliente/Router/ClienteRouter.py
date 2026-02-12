from fastapi import APIRouter, Depends, HTTPException, status
from functools import wraps
from sqlalchemy.orm import Session
from src.config.database import get_db

from src.Cliente.Servicio import ClienteModel, ClienteServicio


route = APIRouter()

rutaBase = f"/cliente"

def handle_exceptions(async_func):
    """Decorador para manejar excepciones de manera uniforme"""
    @wraps(async_func)
    async def wrapper(*args, **kwargs):
        try:
            return await async_func(*args, **kwargs)
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            # Aquí puedes agregar logging: logger.error(f"Error en {async_func.__name__}: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error interno del servidor: {str(e)}"
            )
    return wrapper

@route.post(f"{rutaBase}/crear",
            response_model=ClienteModel.clienteResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Crea cliente nuevo",
            tags=["Clientes"]
            )
@handle_exceptions
async def crear_cliente(cliente: ClienteModel.clienteNew, db: Session = Depends(get_db)):
    """
    Crea un nuevo cliente en la base de datos.

    Args:
        cliente (ClienteModel.clienteNew): Datos del cliente a crear.
        db (Session): Sesión de base de datos inyectada por dependencia.

    Returns:
        ClienteModel.clienteResponse: El cliente creado con su ID asignado.
    """
    new_cliente = await ClienteServicio.add_clienteService(db, cliente)
    return new_cliente

    
@route.post(
            f"{rutaBase}/crearAplicacion",
            response_model=ClienteModel.aplicationResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Crea una aplicacion para un cliente",
            tags=["Clientes"]
            )
@handle_exceptions
async def crear_aplicacion(aplicacion: ClienteModel.aplicacionNew, db: Session = Depends(get_db)):
    """
    Crea una nueva aplicación para un cliente existente.

    Returns:
        ClienteModel.aplicationResponse: La aplicación creada con su ID asignado.
    """
    new_aplicacion = await ClienteServicio.add_aplicacionService(db=db, aplicacion=aplicacion)
    return new_aplicacion
    
@route.get(
        f"{rutaBase}/obtener",
        response_model=ClienteModel.clienteResponse,
        status_code=status.HTTP_200_OK,
        summary="Obtiene datos del cliente a traves del UUID",
        tags=["Clientes"]
        )
@handle_exceptions
async def getCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    """
    Obtiene un cliente por su UUID.

    Returns:
        ClienteModel.clienteResponse: El cliente encontrado.
    """
    unCliente = await ClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
    return unCliente

@route.get(
        f"{rutaBase}/obtenerAplicaciones", 
        response_model=ClienteModel.clienteAppResponse,
        status_code=status.HTTP_200_OK,
        summary="Obtener datos de las aplicaciones de un cliente a traves del UUID",
        tags=["Clientes"]
        )
@handle_exceptions
async def getCLienteAPP(cliente_uuid: str, db: Session = Depends(get_db)):
    """
    Obtiene un cliente con sus aplicaciones por su UUID.

    Returns:
        ClienteModel.clienteAppResponse: El cliente con sus aplicaciones.
    """
    unCliente = await ClienteServicio.get_clienteService(db, cliente_uuid=cliente_uuid)
    return unCliente
    
@route.delete(
        f"{rutaBase}/borrar", 
        response_model=ClienteModel.ServiceResponseBase,
        status_code=status.HTTP_200_OK,
        summary="Eliminar un cliente a traves del UUID",
        tags=["Clientes"],
        )
@handle_exceptions
async def delCliente(cliente_uuid: str, db: Session = Depends(get_db)):
    """
    Elimina un cliente por su UUID.

    Returns:
        ClienteModel.ServiceResponseBase: Confirmación de eliminación.
    """
    result = await ClienteServicio.del_clienteService(db=db, cliente_uuid=cliente_uuid)
    return result
    
@route.patch(
        f"{rutaBase}/vigencia", 
        response_model=ClienteModel.clienteResponse,
        status_code=status.HTTP_200_OK,
        summary="Actualizar la vigencia de un cliente",
        tags=["Clientes"]
        )
@handle_exceptions
async def updVigencia(clienteRequest: ClienteModel.updClienteRequest, db: Session = Depends(get_db)):
    """
    Actualiza la vigencia de un cliente.

    Returns:
        ClienteModel.clienteResponse: El cliente actualizado.
    """
    unCliente = await ClienteServicio.udp_ClienteService(db=db, clienteRequest=clienteRequest)
    return unCliente