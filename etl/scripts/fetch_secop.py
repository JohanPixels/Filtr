import json

import requests

BASE_URL = "https://www.datos.gov.co/resource/jbjy-vk9h.json"
LIMIT = 1000
DEPARTAMENTO = "Huila"


def fetch_secop(BASE_URL, LIMIT, DEPARTAMENTO):
    offset = 0
    counter = 0
    with open("../data/raw_huila.jsonl", "w") as f:
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

            offset += LIMIT

            for record in datos:
                f.write(json.dumps(record) + "\n")
                counter += 1
    print(f"Total records fetched: {counter}")


if __name__ == "__main__":
    fetch_secop(BASE_URL, LIMIT, DEPARTAMENTO)
