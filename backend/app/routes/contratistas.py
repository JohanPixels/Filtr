from database import get_db
from fastapi import APIRouter, Depends
from schemas.contratista import Contratista

router = APIRouter(prefix="/api/v1/contratistas", tags=["Contratistas"])


@router.get("/", response_model=list[Contratista])
async def get_contratistas(skip: int = 0, limit: int = 10, conn=Depends(get_db)):
    with conn.cursor() as cur:
        cur.execute("SELECT * from contratistas LIMIT %s OFFSET %s", (limit, skip))
        return cur.fetchall()
