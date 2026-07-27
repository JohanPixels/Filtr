from database import get_db
from fastapi import APIRouter, Depends
from schemas.contrato import Contrato
from datetime import date

router = APIRouter(prefix="/api/v1/contratos", tags=["Contratos"])


@router.get("/", response_model=list[Contrato])
async def get_contratos(fecha_min: date | None = None, fecha_max: date | None = None, valor_min: int | None = None, valor_max: int | None = None, skip: int = 0, limit: int = 10, conn=Depends(get_db)):
    with conn.cursor() as cur:
        condiciones = []
        valores = []

        if valor_min is not None:
            condiciones.append("valor_contrato >= %s")
            valores.append(valor_min)
        if valor_max is not None:
            condiciones.append("valor_contrato <= %s")
            valores.append(valor_max)
        if fecha_min is not None:
            condiciones.append("fecha_firma >= %s")
            valores.append(fecha_min)
        if fecha_max is not None:
            condiciones.append("fecha_firma <= %s")
            valores.append(fecha_max)

        where_clause = ""

        if condiciones:
            where_clause = "WHERE " + " AND ".join(condiciones)

        query = f"SELECT * FROM contratos {where_clause} LIMIT %s OFFSET %s"
        valores.append(limit)
        valores.append(skip)
        cur.execute(query, valores)


        return cur.fetchall()
