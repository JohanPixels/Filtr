import re

INVALID_VALUES = {"NO DEFINIDO", "SIN DESCRIPCION"}


def is_invalid(value):
    return isinstance(value, str) and value.upper() in INVALID_VALUES


def normalize_str(value) -> str | None:
    if value is None:
        return None
    return str(value).strip().upper() or None


def normalize_date(value):
    if not value:
        return None

    date = re.search(r"\d{4}-\d{2}-\d{2}", value)
    return date.group() if date else None


def clean_entidades(record):
    # Obtener los campos de entidad
    entidad_cleaned = {
        "nombre_entidad": normalize_str(record.get("nombre_entidad")),
        "nit_entidad": record.get("nit_entidad"),
        "departamento": normalize_str(record.get("departamento")),
        "ciudad": normalize_str(record.get("ciudad")),
        "localizacion": normalize_str(record.get("localizaci_n")),
        "orden": normalize_str(record.get("orden")),
        "sector": normalize_str(record.get("sector")),
        "rama": normalize_str(record.get("rama")),
        "entidad_centralizada": normalize_str(record.get("entidad_centralizada")),
    }

    for campo in entidad_cleaned:
        if is_invalid(entidad_cleaned[campo]):
            entidad_cleaned[campo] = None

    return entidad_cleaned


def clean_contratos(record):
    contrato_cleaned = {
        "id_contrato": normalize_str(record.get("id_contrato")),
        "proceso_compra": normalize_str(record.get("proceso_de_compra")),
        "referencia_contrato": normalize_str(record.get("referencia_del_contrato")),
        "estado_contrato": normalize_str(record.get("estado_contrato")),
        "codigo_categoria_principal": normalize_str(
            record.get("codigo_de_categoria_principal")
        ),
        "descripcion_proceso": normalize_str(record.get("descripcion_del_proceso")),
        "tipo_contrato": normalize_str(record.get("tipo_de_contrato")),
        "modalidad_contratacion": normalize_str(
            record.get("modalidad_de_contratacion")
        ),
        "justificacion_modalidad": normalize_str(
            record.get("justificacion_modalidad_de")
        ),
        "fecha_firma": normalize_date(record.get("fecha_de_firma")),
        "fecha_inicio_contrato": normalize_date(
            record.get("fecha_de_inicio_del_contrato")
        ),
        "fecha_fin_contrato": normalize_date(record.get("fecha_de_fin_del_contrato")),
        "liquidacion": normalize_str(record.get("liquidaci_n")),
        "origen_recursos": normalize_str(record.get("origen_de_los_recursos")),
        "destino_gasto": normalize_str(record.get("destino_gasto")),
        "valor_contrato": record.get("valor_del_contrato"),
        "valor_pago_adelantado": record.get("valor_de_pago_adelantado"),
        "valor_facturado": record.get("valor_facturado"),
        "valor_pendiente_pago": record.get("valor_pendiente_de_pago"),
        "valor_pagado": record.get("valor_pagado"),
        "valor_pendiente_ejecucion": record.get("valor_pendiente_de_ejecucion"),
        "saldo_cdp": record.get("saldo_cdp"),
        "saldo_vigencia": record.get("saldo_vigencia"),
        "urlproceso": record.get("urlproceso"),
        "presupuesto_general_nacion": record.get(
            "presupuesto_general_de_la_nacion_pgn"
        ),
        "sistema_general_participaciones": record.get(
            "sistema_general_de_participaciones"
        ),
        "sistema_general_regalias": record.get("sistema_general_de_regal_as"),
        "objeto_contrato": normalize_str(record.get("objeto_del_contrato")),
        "duracion_contrato": record.get("duraci_n_del_contrato"),
        "ultima_actualizacion": normalize_date(record.get("ultima_actualizacion")),
        "codigo_entidad": normalize_str(record.get("codigo_entidad")),
        "codigo_proveedor": normalize_str(record.get("codigo_proveedor")),
        "nombre_supervisor": normalize_str(record.get("nombre_supervisor")),
        "tipo_documento_supervisor": normalize_str(
            record.get("tipo_de_documento_supervisor")
        ),
        "numero_documento_supervisor": normalize_str(
            record.get("numero_de_documento_supervisor")
        ),
    }

    for campo in contrato_cleaned:
        if is_invalid(contrato_cleaned[campo]):
            contrato_cleaned[campo] = None

    # Extraer URL del campo urlproceso
    url_obj = record.get("urlproceso")
    contrato_cleaned["urlproceso"] = url_obj.get("url") if url_obj else None

    # Transformar liquidacion a booleano
    liq = contrato_cleaned["liquidacion"]
    if liq and liq.upper() == "SI":
        contrato_cleaned["liquidacion"] = True
    elif liq and liq.upper() == "NO":
        contrato_cleaned["liquidacion"] = False
    else:
        contrato_cleaned["liquidacion"] = None

    # Extraer numero de dias de duracion del contrato
    duracion_raw = contrato_cleaned.get("duracion_contrato")
    duracion_match = re.search(r"\d+", duracion_raw) if duracion_raw else None
    if duracion_match:
        duracion = int(duracion_match.group())
        contrato_cleaned["duracion_contrato"] = duracion
    else:
        contrato_cleaned["duracion_contrato"] = None

    # Convertir strings de numeros a enteros
    for campo in contrato_cleaned:
        if campo in [
            "valor_contrato",
            "valor_pago_adelantado",
            "valor_facturado",
            "valor_pendiente_pago",
            "valor_pagado",
            "valor_pendiente_ejecucion",
            "saldo_cdp",
            "saldo_vigencia",
            "presupuesto_general_nacion",
            "sistema_general_participaciones",
            "sistema_general_regalias",
        ]:
            contrato_cleaned[campo] = int(contrato_cleaned[campo] or 0)

    return contrato_cleaned


def clean_contratistas(record):
    contratista_cleaned = {
        "tipodocproveedor": normalize_str(record.get("tipodocproveedor")),
        "documento_proveedor": normalize_str(record.get("documento_proveedor")),
        "proveedor_adjudicado": normalize_str(record.get("proveedor_adjudicado")),
        "nombre_representante_legal": normalize_str(
            record.get("nombre_representante_legal")
        ),
        "nacionalidad_representante_legal": normalize_str(
            record.get("nacionalidad_representante_legal")
        ),
        "domicilio_representante_legal": normalize_str(
            record.get("domicilio_representante_legal")
        ),
        "tipo_identificacion_representante_legal": normalize_str(
            record.get("tipo_de_identificaci_n_representante_legal")
        ),
        "identificacion_representante_legal": normalize_str(
            record.get("identificaci_n_representante_legal")
        ),
        "genero_representante_legal": normalize_str(
            record.get("g_nero_representante_legal")
        ),
    }

    for campo in contratista_cleaned:
        if is_invalid(contratista_cleaned[campo]):
            contratista_cleaned[campo] = None

    return contratista_cleaned


def transform_records(records):

    for record in records:
        yield {
            "entidad": clean_entidades(record),
            "contrato": clean_contratos(record),
            "contratista": clean_contratistas(record),
        }
