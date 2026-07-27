from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel


class FlagRiesgo(BaseModel):
    id_flag: int
    id_contrato: Optional[int] = None
    id_contratista: Optional[int] = None
    tipo_flag: Optional[str] = None
    fecha_constitucion_rues: Optional[date] = None
    dias_diferencia: Optional[int] = None
    severidad: Optional[Literal["baja", "media", "alta", "critica"]] = None
    descripcion: Optional[str] = None
