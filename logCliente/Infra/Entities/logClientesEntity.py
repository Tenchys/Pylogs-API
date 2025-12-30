from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base

class cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    uuid = Column(String)
    vigencia = Column(Boolean)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    
