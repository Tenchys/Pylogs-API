from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base

class log(Base):
    __tablename__ = "logs_nuevo"
    id = Column(Integer, primary_key=True, index=True)
    mensaje = Column(String)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    alerta = Column(Boolean, default=False)
    infologs = relationship("infolog", back_populates="log", cascade="all, delete-orphan")



class infolog(Base):
    __tablename__ = "infolog"
    id = Column(Integer, primary_key=True, index=True)
    nombre_alerta = Column(String, nullable=False)
    valor_alerta = Column(String(500), nullable= False)
    log_id = Column(Integer, ForeignKey("logs_nuevo.id"), nullable=False)

    log = relationship("log", back_populates="infologs")
