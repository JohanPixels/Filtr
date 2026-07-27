from typing import Optional

from pydantic import BaseModel


class Entidad(BaseModel):
    entidad_id: int
    nombre_entidad: Optional[str] = None
    nit_entidad: str
    departamento: Optional[str] = None
    ciudad: Optional[str] = None
    localizacion: Optional[str] = None
    orden: Optional[str] = None
    sector: Optional[str] = None
    rama: Optional[str] = None
    entidad_centralizada: Optional[str] = None
