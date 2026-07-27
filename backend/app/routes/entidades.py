from database import get_db
from fastapi import APIRouter, Depends
from schemas.entidad import Entidad

router = APIRouter(prefix="/api/v1/entidades", tags=["Entidades"])


@router.get("/", response_model=list[Entidad])
async def get_entidades(
    ciudad: str | None = None, departamento: str | None = None, skip: int = 0, limit: int = 10, conn=Depends(get_db)
):
    with conn.cursor() as cur:
        condiciones = []
        valores = []

        if ciudad:
            condiciones.append("unaccent(ciudad) ILIKE unaccent(%s)")
            valores.append(ciudad)

        if departamento:
            condiciones.append("unaccent(departamento) ILIKE unaccent(%s)")
            valores.append(departamento)

        where_clause = ""

        if condiciones:
            where_clause = "WHERE " + " AND ".join(condiciones)
        query = f"SELECT * FROM entidades {where_clause} LIMIT %s OFFSET %s"
        valores.append(limit)
        valores.append(skip)

        cur.execute(query, valores)
        return cur.fetchall()
