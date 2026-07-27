from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Contrato(BaseModel):
    id: int
    id_contrato: str
    proceso_compra: Optional[str] = None
    referencia_contrato: Optional[str] = None
    estado_contrato: Optional[str] = None
    codigo_categoria_principal: Optional[str] = None
    descripcion_proceso: Optional[str] = None
    tipo_contrato: Optional[str] = None
    modalidad_contratacion: Optional[str] = None
    justificacion_modalidad: Optional[str] = None
    fecha_firma: Optional[datetime] = None
    fecha_inicio_contrato: Optional[datetime] = None
    fecha_fin_contrato: Optional[datetime] = None
    liquidacion: Optional[bool] = None
    origen_recursos: Optional[str] = None
    destino_gasto: Optional[str] = None
    valor_contrato: Optional[int] = None
    valor_pago_adelantado: Optional[int] = None
    valor_facturado: Optional[int] = None
    valor_pendiente_pago: Optional[int] = None
    valor_pagado: Optional[int] = None
    valor_pendiente_ejecucion: Optional[int] = None
    saldo_cdp: Optional[int] = None
    saldo_vigencia: Optional[int] = None
    urlproceso: Optional[str] = None
    presupuesto_general_nacion: Optional[int] = None
    sistema_general_participaciones: Optional[int] = None
    sistema_general_regalias: Optional[int] = None
    objeto_contrato: Optional[str] = None
    duracion_contrato: Optional[int] = None
    ultima_actualizacion: Optional[datetime] = None
    codigo_entidad: Optional[str] = None
    codigo_proveedor: Optional[str] = None
    nombre_supervisor: Optional[str] = None
    tipo_documento_supervisor: Optional[str] = None
    numero_documento_supervisor: Optional[str] = None
    entidad_id: Optional[int] = None
    contratista_id: Optional[int] = None
