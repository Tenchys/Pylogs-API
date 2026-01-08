from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.config.database import Base

class cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    uuid = Column(String, unique=True)
    vigencia = Column(Boolean)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    aplicaciones = relationship("aplicacion", back_populates="cliente", cascade="all, delete-orphan")



class aplicacion(Base):
    __tablename__ = "aplicaciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    uuid = Column(String, unique=True)
    vigencia = Column(Boolean)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    cliente_uuid = Column(String, ForeignKey("clientes.uuid"), nullable=False)  

    cliente = relationship("cliente", back_populates="aplicaciones")
