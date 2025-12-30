from pydantic import BaseModel


class clienteBase(BaseModel):
    nombre: str
    vigencia: bool

class clienteNew(clienteBase):
    pass

class clienteResponse(clienteBase):
    uuid: str