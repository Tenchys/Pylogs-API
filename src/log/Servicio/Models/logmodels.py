from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class logBase(BaseModel):
    mensaje: str
    alerta: bool = False

class infologBase(BaseModel):
    nombre_alerta: str
    valor_alerta: str

class infologCreate(infologBase):
    pass

class infologResponse(infologBase):
    pass
    model_config = {"from_attributes": True}

class logCreate(logBase):
    uuid: str
    infologs: Optional[List[infologCreate]] = None

class logResponse(logBase):
    id: int
    fecha_creacion: datetime

class logsInfoLogResponse(logResponse):
    infologs: Optional[List[infologResponse]]
    model_config = {"from_attributes": True}


