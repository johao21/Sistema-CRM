from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeadBase(BaseModel):
    nombre: str
    telefono: str
    correo: Optional[str] = None
    servicio: str
    estado_id: int
    notas_generales: Optional[str] = None

class LeadCreate(LeadBase):
    pass

class LeadResponse(LeadBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True