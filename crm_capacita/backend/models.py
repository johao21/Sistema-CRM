from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Estado(Base):
    __tablename__ = "estados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    correo = Column(String(100))
    servicio = Column(String(100), nullable=False)
    estado_id = Column(Integer, ForeignKey("estados.id"), nullable=False)
    notas_generales = Column(Text)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())