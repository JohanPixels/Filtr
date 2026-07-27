from typing import Optional

from pydantic import BaseModel


class Contratista(BaseModel):
    contratista_id: int
    tipodocproveedor: Optional[str] = None
    documento_proveedor: str
    proveedor_adjudicado: Optional[str] = None
    nombre_representante_legal: Optional[str] = None
    nacionalidad_representante_legal: Optional[str] = None
    domicilio_representante_legal: Optional[str] = None
    tipo_identificacion_representante_legal: Optional[str] = None
    identificacion_representante_legal: Optional[str] = None
    genero_representante_legal: Optional[str] = None
