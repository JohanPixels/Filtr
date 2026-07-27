from datetime import date

from fastapi import APIRouter, Depends

from database import get_db
from schemas.dashboard_stats import DashboardStats, RangoFechas

router = APIRouter(prefix="/api/v1/dashboard", tags=["Dashboard"])

@router.get("/", response_model=DashboardStats)
async def get_dashboard_stats(conn=Depends(get_db)):
    with conn.cursor() as cur:
        # Resumen general
        cur.execute("""
            SELECT COUNT(*) AS total_contratos,
            SUM(valor_contrato) AS valor_total_contratos,
            AVG(valor_contrato) AS valor_promedio_contratos
            FROM contratos
        """)
        row = cur.fetchone()
        total_contratos = row["total_contratos"]
        valor_total_contratos = row["valor_total_contratos"] or 0
        valor_promedio_contrato = row["valor_promedio_contratos"] or 0

        # total entidades
        cur.execute("""
            SELECT COUNT(*) AS total_entidades
            FROM entidades
            """)
        row = cur.fetchone()
        total_entidades = row["total_entidades"]

        # total contratistas
        cur.execute("""
            SELECT COUNT(*) AS total_contratistas
            FROM contratistas
        """)
        row = cur.fetchone()
        total_contratistas = row["total_contratistas"]

        # Señales de riesgo
        cur.execute("""
            SELECT COUNT(*) AS contratistas_sin_documento
            FROM contratistas
            WHERE documento_proveedor LIKE 'SINID-%'
        """)
        row = cur.fetchone()
        contratistas_sin_documento = row["contratistas_sin_documento"]

        # Distribucion
        cur.execute("""
            SELECT modalidad_contratacion, COUNT(*) AS total
            FROM contratos
            GROUP BY modalidad_contratacion
        """)
        contratos_por_modalidad = {row["modalidad_contratacion"]: row["total"] for row in cur.fetchall()}
        # Rango de fechas
        cur.execute("""
            SELECT MIN(fecha_firma) AS fecha_minima_contrato,
            MAX(fecha_firma) AS fecha_maxima_contrato
            FROM contratos
        """)
        row = cur.fetchone()
        fecha_minima_contrato = row["fecha_minima_contrato"]
        fecha_maxima_contrato = row["fecha_maxima_contrato"]

        rango_fechas = RangoFechas(
            fecha_minima_contrato=fecha_minima_contrato,
            fecha_maxima_contrato=fecha_maxima_contrato
        )

        return DashboardStats(
            total_contratos=total_contratos,
            valor_total_contratos=valor_total_contratos,
            total_entidades=total_entidades,
            total_contratistas=total_contratistas,
            valor_promedio_contrato=valor_promedio_contrato,
            contratistas_sin_documento=contratistas_sin_documento,
            contratos_por_modalidad=contratos_por_modalidad,
            rango_fechas=rango_fechas
        )
