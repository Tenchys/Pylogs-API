from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.database import Base

class log(Base):
    __tablename__ = "logs_nuevo"
    id = Column(Integer, primary_key=True, index=True)
    mensaje = Column(String)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    alerta = Column(Boolean, default=False)