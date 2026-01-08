from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ServiceResponseBase(BaseModel):
    mensaje: str


class clienteBase(BaseModel):
    nombre: str
    vigencia: bool

class applicacionBase(BaseModel):
    nombre: str
    vigencia: bool

class clienteNew(clienteBase):
    pass

class aplicacionNew(applicacionBase):
    cliente_uuid: str


class aplicationResponse(applicacionBase):
    uuid: str
    cliente_uuid: str
    fecha_creacion: datetime
    model_config = {"from_attributes": True}


class clienteResponse(clienteBase):
    uuid: str

class clienteAppResponse(clienteResponse):
    aplicaciones: list[aplicationResponse] = []

class updClienteRequest(clienteBase):
    uuid: str
    nombre: Optional[str] = None
    vigencia: Optional[bool] = None

