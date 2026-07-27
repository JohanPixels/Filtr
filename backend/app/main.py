from fastapi import FastAPI
from routes import contratistas, contratos, entidades, dashboard
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(contratos.router)
app.include_router(contratistas.router)
app.include_router(entidades.router)
app.include_router(dashboard.router)

@app.get("/")
async def root():
    return {"message": "Hola Filtr :D"}
