from datetime import datetime
from pydantic import BaseModel

class logBase(BaseModel):
    mensaje: str
    alerta: bool = False

class logCreate(logBase):
    pass

class logResponse(logBase):
    id: int
    fecha_creacion: datetime