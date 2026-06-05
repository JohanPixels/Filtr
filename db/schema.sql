CREATE TABLE entidades (
    entidad_id SERIAL PRIMARY KEY,
    nombre_entidad VARCHAR,
    nit_entidad VARCHAR UNIQUE NOT NULL,
    departamento VARCHAR,
    ciudad VARCHAR,
    localizacion VARCHAR,
    orden VARCHAR,
    sector VARCHAR,
    rama VARCHAR,
    entidad_centralizada VARCHAR
);

CREATE TABLE contratos (
    id SERIAL PRIMARY KEY,
    id_contrato VARCHAR UNIQUE NOT NULL,
    proceso_compra VARCHAR,
    referencia_contrato VARCHAR,
    estado_contrato VARCHAR,
    codigo_categoria_principal VARCHAR,
    descripcion_proceso TEXT,
    tipo_contrato VARCHAR,
    modalidad_contratacion VARCHAR,
    justificacion_modalidad VARCHAR,
    fecha_firma TIMESTAMP,
    fecha_inicio_contrato TIMESTAMP,
    fecha_fin_contrato TIMESTAMP,
    liquidacion BOOLEAN,
    origen_recursos VARCHAR,
    destino_gasto VARCHAR,
    valor_contrato BIGINT,
    valor_pago_adelantado BIGINT,
    valor_facturado BIGINT,
    valor_pendiente_pago BIGINT,
    valor_pagado BIGINT,
    valor_pendiente_ejecucion BIGINT,
    saldo_cdp BIGINT,
    saldo_vigencia BIGINT,
    urlproceso TEXT,
    presupuesto_general_nacion BIGINT,
    sistema_general_participaciones BIGINT,
    sistema_general_regalias BIGINT,
    objeto_contrato TEXT,
    duracion_contrato INT,
    ultima_actualizacion TIMESTAMP,
    codigo_entidad VARCHAR,
    codigo_proveedor VARCHAR,
    nombre_supervisor VARCHAR,
    tipo_documento_supervisor VARCHAR,
    numero_documento_supervisor VARCHAR,

    entidad_id INT,
    contratista_id INT,
    FOREIGN KEY (entidad_id) REFERENCES entidades(entidad_id),
    FOREIGN KEY (contratista_id) REFERENCES contratistas(contratista_id)
);

CREATE TABLE contratistas (
    contratista_id SERIAL PRIMARY KEY,
    tipodocproveedor VARCHAR,
    documento_proveedor VARCHAR UNIQUE NOT NULL,
    proveedor_adjudicado VARCHAR,
    nombre_representante_legal VARCHAR,
    nacionalidad_representante_legal CHAR,
    domicilio_representante_legal VARCHAR,
    tipo_identificacion_representante_legal VARCHAR,
    identificacion_representante_legal VARCHAR,
    genero_representante_legal VARCHAR
);

CREATE TABLE flags_riesgo (
    id_flag SERIAL PRIMARY KEY,
    id_contrato INT,
    id_contratista INT,
    tipo_flag VARCHAR,
    fecha_constitucion_rues DATE,
    dias_diferencia INT,
    severidad VARCHAR CHECK (severidad IN ('baja', 'media', 'alta', 'critica')),
    descripcion TEXT,

    FOREIGN KEY (id_contrato) REFERENCES contratos(id),
    FOREIGN KEY (id_contratista) REFERENCES contratistas(contratista_id)
)
