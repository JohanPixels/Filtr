from pydantic import BaseModel
from datetime import date

class RangoFechas(BaseModel):
    fecha_minima_contrato: date
    fecha_maxima_contrato: date

class DashboardStats(BaseModel):
    # Resumen general
    # top_departamentos,
    total_contratos: int
    valor_total_contratos: float
    total_entidades: int
    total_contratistas: int
    valor_promedio_contrato: float

    # Señales de riesgo
    contratistas_sin_documento: int

    # Distribucion
    contratos_por_modalidad: dict[str, int]
    rango_fechas: RangoFechas
