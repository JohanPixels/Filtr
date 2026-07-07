import os

import psycopg
from dotenv import load_dotenv
from fetch_secop import BASE_URL, DEPARTAMENTO, LIMIT, fetch_secop
from psycopg.rows import dict_row
from transform import normalize_str, transform_records

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
dbname = os.getenv("POSTGRES_DB")


def load_data(records):

    with psycopg.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port,
    ) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            contador_commits = 0
            for record in records:
                entidad_temp = record["entidad"]
                contrato_temp = record["contrato"]
                contratista_temp = record["contratista"]
                entidad_id = None

                # Carga de entidades
                (
                    nombre_entidad,
                    nit_entidad,
                    departamento,
                    ciudad,
                    localizacion,
                    orden,
                    sector,
                    rama,
                    entidad_centralizada,
                ) = (
                    entidad_temp["nombre_entidad"],
                    entidad_temp["nit_entidad"],
                    entidad_temp["departamento"],
                    entidad_temp["ciudad"],
                    entidad_temp["localizacion"],
                    entidad_temp["orden"],
                    entidad_temp["sector"],
                    entidad_temp["rama"],
                    entidad_temp["entidad_centralizada"],
                )

                cur.execute(
                    """
                    INSERT INTO entidades (nombre_entidad, nit_entidad, departamento, ciudad, localizacion, orden, sector, rama, entidad_centralizada)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (nit_entidad)
                    DO UPDATE SET nit_entidad = EXCLUDED.nit_entidad
                    RETURNING entidad_id
                    """,
                    (
                        nombre_entidad,
                        nit_entidad,
                        departamento,
                        ciudad,
                        localizacion,
                        orden,
                        sector,
                        rama,
                        entidad_centralizada,
                    ),
                )
                resultado_entidad = cur.fetchone()
                assert resultado_entidad is not None

                entidad_id = resultado_entidad["entidad_id"]

                contratista_id = None

                # Carga de contratistas
                if (
                    contratista_temp["documento_proveedor"] is None
                    and contratista_temp["proveedor_adjudicado"] is not None
                ):
                    contratista_temp["documento_proveedor"] = (
                        f"SINID-{normalize_str(contratista_temp['proveedor_adjudicado'])}"
                    )

                if contratista_temp["tipodocproveedor"] is not None:
                    (
                        tipodocproveedor,
                        documento_proveedor,
                        proveedor_adjudicado,
                        nombre_representante_legal,
                        nacionalidad_representante_legal,
                        domicilio_representante_legal,
                        tipo_identificacion_representante_legal,
                        identificacion_representante_legal,
                        genero_representante_legal,
                    ) = (
                        contratista_temp["tipodocproveedor"],
                        contratista_temp["documento_proveedor"],
                        contratista_temp["proveedor_adjudicado"],
                        contratista_temp["nombre_representante_legal"],
                        contratista_temp["nacionalidad_representante_legal"],
                        contratista_temp["domicilio_representante_legal"],
                        contratista_temp["tipo_identificacion_representante_legal"],
                        contratista_temp["identificacion_representante_legal"],
                        contratista_temp["genero_representante_legal"],
                    )

                    cur.execute(
                        """
                        INSERT INTO contratistas (tipodocproveedor, documento_proveedor, proveedor_adjudicado, nombre_representante_legal, nacionalidad_representante_legal, domicilio_representante_legal, tipo_identificacion_representante_legal, identificacion_representante_legal, genero_representante_legal)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (documento_proveedor)
                        DO UPDATE SET documento_proveedor = EXCLUDED.documento_proveedor
                        RETURNING contratista_id
                        """,
                        (
                            tipodocproveedor,
                            documento_proveedor,
                            proveedor_adjudicado,
                            nombre_representante_legal,
                            nacionalidad_representante_legal,
                            domicilio_representante_legal,
                            tipo_identificacion_representante_legal,
                            identificacion_representante_legal,
                            genero_representante_legal,
                        ),
                    )
                    resultado_contratista = cur.fetchone()
                    assert resultado_contratista is not None
                    contratista_id = resultado_contratista["contratista_id"]

                # Carga de contratos
                (
                    id_contrato,
                    proceso_compra,
                    referencia_contrato,
                    estado_contrato,
                    codigo_categoria_principal,
                    descripcion_proceso,
                    tipo_contrato,
                    modalidad_contratacion,
                    justificacion_modalidad,
                    fecha_firma,
                    fecha_inicio_contrato,
                    fecha_fin_contrato,
                    liquidacion,
                    origen_recursos,
                    destino_gasto,
                    valor_contrato,
                    valor_pago_adelantado,
                    valor_facturado,
                    valor_pendiente_pago,
                    valor_pagado,
                    valor_pendiente_ejecucion,
                    saldo_cdp,
                    saldo_vigencia,
                    urlproceso,
                    presupuesto_general_nacion,
                    sistema_general_participaciones,
                    sistema_general_regalias,
                    objeto_contrato,
                    duracion_contrato,
                    ultima_actualizacion,
                    codigo_entidad,
                    codigo_proveedor,
                    nombre_supervisor,
                    tipo_documento_supervisor,
                    numero_documento_supervisor,
                ) = (
                    contrato_temp["id_contrato"],
                    contrato_temp["proceso_compra"],
                    contrato_temp["referencia_contrato"],
                    contrato_temp["estado_contrato"],
                    contrato_temp["codigo_categoria_principal"],
                    contrato_temp["descripcion_proceso"],
                    contrato_temp["tipo_contrato"],
                    contrato_temp["modalidad_contratacion"],
                    contrato_temp["justificacion_modalidad"],
                    contrato_temp["fecha_firma"],
                    contrato_temp["fecha_inicio_contrato"],
                    contrato_temp["fecha_fin_contrato"],
                    contrato_temp["liquidacion"],
                    contrato_temp["origen_recursos"],
                    contrato_temp["destino_gasto"],
                    contrato_temp["valor_contrato"],
                    contrato_temp["valor_pago_adelantado"],
                    contrato_temp["valor_facturado"],
                    contrato_temp["valor_pendiente_pago"],
                    contrato_temp["valor_pagado"],
                    contrato_temp["valor_pendiente_ejecucion"],
                    contrato_temp["saldo_cdp"],
                    contrato_temp["saldo_vigencia"],
                    contrato_temp["urlproceso"],
                    contrato_temp["presupuesto_general_nacion"],
                    contrato_temp["sistema_general_participaciones"],
                    contrato_temp["sistema_general_regalias"],
                    contrato_temp["objeto_contrato"],
                    contrato_temp["duracion_contrato"],
                    contrato_temp["ultima_actualizacion"],
                    contrato_temp["codigo_entidad"],
                    contrato_temp["codigo_proveedor"],
                    contrato_temp["nombre_supervisor"],
                    contrato_temp["tipo_documento_supervisor"],
                    contrato_temp["numero_documento_supervisor"],
                )

                cur.execute(
                    """
                INSERT INTO contratos (id_contrato, proceso_compra, referencia_contrato, estado_contrato, codigo_categoria_principal, descripcion_proceso, tipo_contrato, modalidad_contratacion, justificacion_modalidad, fecha_firma, fecha_inicio_contrato, fecha_fin_contrato, liquidacion, origen_recursos, destino_gasto, valor_contrato, valor_pago_adelantado, valor_facturado, valor_pendiente_pago, valor_pagado, valor_pendiente_ejecucion, saldo_cdp, saldo_vigencia, urlproceso, presupuesto_general_nacion, sistema_general_participaciones, sistema_general_regalias, objeto_contrato, duracion_contrato, ultima_actualizacion, codigo_entidad, codigo_proveedor, nombre_supervisor, tipo_documento_supervisor, numero_documento_supervisor, entidad_id, contratista_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id_contrato)
                DO UPDATE SET id_contrato = EXCLUDED.id_contrato
                RETURNING id
                """,
                    (
                        id_contrato,
                        proceso_compra,
                        referencia_contrato,
                        estado_contrato,
                        codigo_categoria_principal,
                        descripcion_proceso,
                        tipo_contrato,
                        modalidad_contratacion,
                        justificacion_modalidad,
                        fecha_firma,
                        fecha_inicio_contrato,
                        fecha_fin_contrato,
                        liquidacion,
                        origen_recursos,
                        destino_gasto,
                        valor_contrato,
                        valor_pago_adelantado,
                        valor_facturado,
                        valor_pendiente_pago,
                        valor_pagado,
                        valor_pendiente_ejecucion,
                        saldo_cdp,
                        saldo_vigencia,
                        urlproceso,
                        presupuesto_general_nacion,
                        sistema_general_participaciones,
                        sistema_general_regalias,
                        objeto_contrato,
                        duracion_contrato,
                        ultima_actualizacion,
                        codigo_entidad,
                        codigo_proveedor,
                        nombre_supervisor,
                        tipo_documento_supervisor,
                        numero_documento_supervisor,
                        entidad_id,
                        contratista_id,
                    ),
                )
                resultado_contrato = cur.fetchone()
                assert resultado_contrato is not None

                contrato_id = resultado_contrato["id"]

                contador_commits += 1

                if contador_commits % 1000 == 0:
                    conn.commit()
                    print(f"Se han procesado {contador_commits} registros.")
            conn.commit()


if __name__ == "__main__":
    load_data(transform_records(fetch_secop(BASE_URL, LIMIT, DEPARTAMENTO)))
