# FILTR — Plan de desarrollo MVP

> **Stack:** FastAPI · Svelte + Vite · PostgreSQL · Docker Compose  
> **Duración estimada:** 4 semanas (4 sprints de ~1 semana c/u)  
> **Objetivo:** Una plataforma de inteligencia pública sobre contratación en Colombia, funcional y desplegada, con datos reales de SECOP II.

---

## Qué entra en el MVP

### Sprint 1 — Datos vivos en la DB

**Objetivo:** Datos reales de SECOP II corriendo en PostgreSQL local.

| Capa | Tarea | Notas |
|------|-------|-------|
| DB | Esquema de base de datos — tablas `contratos`, `entidades`, `contratistas` | Campos: valor, fechas, modalidad, departamento, municipio, estado |
| DB | Tabla `flags_riesgo` — cruce NIT vs fecha de creación en RUES | Empresa creada <90 días antes del contrato = bandera automática |
| ETL | Script que jala contratos de SECOP II API y los carga a PostgreSQL | Arrancar con un solo departamento (ej. Huila) |
| ETL | Limpieza básica: normalizar NIT, parsear fechas, manejar nulos | La data de SECOP viene sucia — esto es crítico |

**Entregable:** Datos reales en PostgreSQL, consultables desde `psql`.

---

### Sprint 2 — API que responde

**Objetivo:** FastAPI respondiendo con datos reales en `localhost:8000`.

| Endpoint | Descripción |
|----------|-------------|
| `GET /contratos` | Búsqueda con filtros: entidad, valor, fecha, departamento. Paginado (máx. 50 resultados) |
| `GET /contratos/{id}/timeline` | Historia completa del contrato: adjudicación → inicio → adiciones → prórrogas → cierre |
| `GET /entidades/{id}` | Perfil de entidad con totales (contratos activos, valor total, histórico) |
| `GET /contratistas/{nit}` | Perfil de empresa con flags de riesgo — cruce con RUES incluido |
| `GET /dashboard` | Totales nacionales y por departamento |

**Entregable:** API testeable con Swagger UI, conectada a datos reales.

---

### Sprint 3 — Frontend que se usa

**Objetivo:** App funcional en `localhost:3000` conectada al backend.

| Pantalla / Componente | Descripción |
|-----------------------|-------------|
| Dashboard home | Cards con totales nacionales + top 5 entidades y contratistas |
| Búsqueda con filtros | Por entidad, departamento, rango de valor, año — resultados en tabla ordenable |
| Vista de contrato | **Línea de tiempo visual** de cada etapa del contrato — la feature más diferenciadora |
| Perfil de contratista | Historial de contratos + badge de riesgo visible (🔴 empresa nueva / 🟡 concentración alta / 🟢 sin banderas) |
| Mapa de Colombia | Mapa coroplético coloreado por volumen de contratación por departamento |

**Entregable:** Interfaz funcional con datos reales, navegable en el browser.

---

### Sprint 4 — Pulir y lanzar

**Objetivo:** Filtr en internet, con URL pública y datos reales de Colombia.

| Tarea | Notas |
|-------|-------|
| Responsive móvil | Periodistas y veedores consultan desde el celular en campo |
| Rate limiting + CORS | Configurado para producción |
| Cron job ETL | Actualización automática de datos cada 24 horas |
| Screenshot / GIF del dashboard | Sin esto nadie abre el repo — es no negociable para el README |
| Deploy | Railway o Render (gratis, suficiente para MVP) |

**Entregable:** URL pública funcional. El proyecto pasa de local a portafolio real.

---

## Lo que NO entra en el MVP (post-MVP / v2)

Estas funcionalidades están definidas y son parte de la visión del producto, pero se construyen **después** de tener usuarios reales dando feedback sobre el MVP.

| Feature | Por qué espera |
|---------|----------------|
| Resumen IA de contratos ("explícame este contrato") | Requiere integración con API externa (OpenAI / Claude) y diseño de prompts |
| Preguntas en lenguaje natural sobre el gasto público | Alta complejidad técnica — depende de tener un modelo afinado o RAG bien construido |
| Alertas y notificaciones por email | Requiere autenticación de usuarios, sistema de colas y proveedor de email |
| Comparador de municipios | Feature valiosa pero no bloquea el MVP |
| Índice de transparencia propio (0–100) | Requiere definir y validar la metodología antes de publicar un score |
| Grafo de relaciones entidad → contrato → empresa | Alta complejidad visual — mejor con usuarios reales para saber qué relaciones importan |
| Participación ciudadana (reportes fotográficos) | Requiere infraestructura de almacenamiento de archivos y moderación |
| Seguimiento de proyectos (avance físico + financiero) | Depende de integrar fuentes externas a SECOP |

---

## La feature diferenciadora del MVP

De todo lo que entra en el sprint 1, hay una que ningún otro visor de SECOP hace:

> **Cruce automático NIT vs RUES:** si una empresa fue creada menos de 90 días antes de recibir un contrato público de alto valor, Filtr lo marca automáticamente como riesgo. Eso es periodismo de datos automatizado.

---

## Regla de desarrollo

> Primero que funcione, luego que impresione.

El MVP lanzado ya es algo que periodistas pueden usar, algo para mostrar en portafolio, y sobre todo — algo que dice qué construir en v2 con información real, no con suposiciones.

---

## Fuentes de datos

| Fuente | Uso |
|--------|-----|
| [SECOP II — datos.gov.co](https://www.datos.gov.co/resource/jbjy-vk9h.json) | Contratos, entidades, contratistas, modificaciones |
| [RUES](https://www.rues.org.co/) | Fecha de constitución de empresas (cruce anti-riesgo) |
| CHIP | Datos fiscales de municipios (post-MVP) |
| Mapa de regalías | Contratos financiados con regalías (post-MVP) |

---

*Documento generado como parte del proceso de planeación de FILTR. Stack: FastAPI + Svelte + PostgreSQL + Docker.*
