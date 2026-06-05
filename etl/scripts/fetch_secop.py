import json

import requests

BASE_URL = "https://www.datos.gov.co/resource/jbjy-vk9h.json"
LIMIT = 1000
DEPARTAMENTO = "Huila"


def fetch_secop(BASE_URL, LIMIT, DEPARTAMENTO):
    offset = 0
    todos_los_datos = []

    while True:
        params = {
            "$limit": LIMIT,
            "$offset": offset,
            "$where": f"departamento='{DEPARTAMENTO}'",
        }
        pagina = requests.get(BASE_URL, params=params)
        datos = pagina.json()

        if len(datos) == 0:
            break

        todos_los_datos += datos
        offset += LIMIT
    return todos_los_datos


if __name__ == "__main__":
    datos = fetch_secop(BASE_URL, LIMIT, DEPARTAMENTO)
    print(
        f"Se han obtenido {len(datos)} registros del SECOP para el departamento de {DEPARTAMENTO}."
    )
    print(datos[0])
    with open("etl/data/raw_huila.json", "w") as f:
        json.dump(
            datos,
            f,
        )
