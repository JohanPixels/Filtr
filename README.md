# FILTR 🔍

> **Español** · [English below](#english-version)

---

## ¿Qué es FILTR?

FILTR es una herramienta de transparencia para datos de contratación pública en Colombia. El SECOP II tiene millones de registros de contratos públicos que técnicamente son abiertos, pero en la práctica son imposibles de consultar. FILTR los hace buscables, filtrables y auditables.

La contratación pública puede parecer transparente. FILTR la hace realmente visible.

## El problema

Colombia publica sus contratos públicos en el SECOP II — una base de datos enorme, oficial y abierta. El problema: la interfaz es lenta, no tiene búsqueda avanzada, y cruzar datos entre entidades es casi imposible. Resultado: la información está disponible para todos, pero útil para nadie.

FILTR resuelve eso.

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | Svelte + Vite |
| Backend | FastAPI + Python |
| Base de datos | PostgreSQL |
| Pipeline ETL | Python (scripts propios) |
| Infraestructura | Docker Compose + Nginx |

## Arquitectura

```
filtr/
│
├── docker-compose.yml          ← orquestación de servicios
├── .env                        ← variables de entorno (no se sube a GitHub)
├── .gitignore
│
├── frontend/                   ← Svelte + Vite
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── App.svelte
│       ├── lib/
│       │   ├── Map.svelte
│       │   ├── Dashboard.svelte
│       │   └── Charts.svelte
│       └── routes/
│
├── backend/                    ← FastAPI
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── models/
│       ├── routes/
│       ├── schemas/
│       └── database.py
│
├── etl/                        ← pipeline de ingesta SECOP
│   ├── Dockerfile
│   ├── requirements.txt
│   └── scripts/
│       ├── fetch_secop.py
│       ├── clean.py
│       └── load.py
│
└── nginx/                      ← reverse proxy
    └── nginx.conf
```

## Cómo correrlo localmente

### Requisitos previos

- Docker y Docker Compose instalados
- Git

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/filtr.git
cd filtr

# 2. Configurar variables de entorno
cp .env.example .env
# Edita .env con tus valores

# 3. Levantar todos los servicios
docker-compose up --build
```

La app estará disponible en `http://localhost:3000`

## Variables de entorno

Crea un archivo `.env` basado en `.env.example`:

```env
# Base de datos
POSTGRES_DB=filtr_db
POSTGRES_USER=filtr_user
POSTGRES_PASSWORD=tu_contraseña_aqui
DATABASE_URL=postgresql://filtr_user:tu_contraseña@db:5432/filtr_db

# Backend
SECRET_KEY=genera_una_clave_secreta_aqui
DEBUG=false

# SECOP API
SECOP_API_URL=https://www.datos.gov.co/resource/jbjy-vk9h.json
```

## Estado del proyecto

- [x] Estructura del proyecto definida
- [x] Arquitectura Docker documentada
- [ ] Pipeline ETL — ingesta desde API SECOP II
- [ ] Modelos de base de datos
- [ ] Endpoints REST (FastAPI)
- [ ] Dashboard frontend (Svelte)
- [ ] Filtros por entidad, departamento, valor y fechas
- [ ] Detección de anomalías
- [ ] Roles de usuario (periodista / auditor / ciudadano)

## Fuente de datos

Los datos provienen del **SECOP II** (Sistema Electrónico de Contratación Pública), administrado por Colombia Compra Eficiente. Son datos públicos y abiertos disponibles en [datos.gov.co](https://www.datos.gov.co/).

## Por qué existe este proyecto

El acceso real a la información pública no debería requerir ser experto en datos. Este proyecto nació de la convicción de que los contratos del Estado le pertenecen a todos los ciudadanos — y que hacerlos verdaderamente legibles es un acto de transparencia.

## Contribuir

El proyecto está en construcción activa. Si quieres contribuir, abre un issue o un PR.

## Licencia

MIT

---

<a name="english-version"></a>

# FILTR 🔍 — English Version

## What is FILTR?

FILTR is a transparency tool for public procurement data in Colombia. SECOP II holds millions of public contract records that are technically open, but practically impossible to query. FILTR makes them searchable, filterable, and auditable.

Public procurement can look transparent. FILTR makes it actually visible.

## The Problem

Colombia publishes its public contracts on SECOP II — a massive, official, open database. The problem: the interface is slow, lacks advanced search, and cross-referencing data between entities is nearly impossible. The result: information is available to everyone, but useful to no one.

FILTR solves that.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Svelte + Vite |
| Backend | FastAPI + Python |
| Database | PostgreSQL |
| ETL Pipeline | Python (custom scripts) |
| Infrastructure | Docker Compose + Nginx |

## How to Run Locally

```bash
git clone https://github.com/your-username/filtr.git
cd filtr
cp .env.example .env
docker-compose up --build
```

App will be available at `http://localhost:3000`

## Project Status

- [x] Project structure defined
- [x] Docker architecture documented
- [ ] ETL pipeline — ingestion from SECOP II API
- [ ] Database models
- [ ] REST endpoints (FastAPI)
- [ ] Frontend dashboard (Svelte)
- [ ] Filters by entity, department, amount, and dates
- [ ] Anomaly detection
- [ ] User roles (journalist / auditor / citizen)

## Data Source

Data comes from **SECOP II** (Sistema Electrónico de Contratación Pública), managed by Colombia Compra Eficiente. It is publicly available at [datos.gov.co](https://www.datos.gov.co/).

## License

MIT
