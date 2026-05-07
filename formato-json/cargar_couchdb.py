import requests
import json
from credenciales import USUARIO, PASSWORD, HOST, PUERTO

URL_BASE = f"http://{USUARIO}:{PASSWORD}@{HOST}:{PUERTO}"
BASE_DATOS = "jugadores"

# 1. Crear base de datos
respuesta = requests.put(f"{URL_BASE}/{BASE_DATOS}")

if respuesta.status_code == 201:
    print("Base de datos jugadores creada correctamente")
elif respuesta.status_code == 412:
    print("La base de datos jugadores ya existe")
else:
    print("Error creando la base de datos:", respuesta.text)

# 2. Leer JSON
with open("mundial_2026.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# 3. Cargar documentos
respuesta = requests.post(
    f"{URL_BASE}/{BASE_DATOS}/_bulk_docs",
    headers={"Content-Type": "application/json"},
    json=datos
)

print("Carga de documentos:", respuesta.status_code)

# 4. Crear vistas automáticamente
design_doc = {
    "_id": "_design/losjugadores",
    "views": {
        "por_club": {
            "map": "function(doc) { if (doc.club_actual) { emit(doc.club_actual, doc); } }"
        },
        "por_goles": {
            "map": "function(doc) { if (doc.goles) { emit(doc.goles, doc); } }"
        },
        "por_partidos": {
            "map": "function(doc) { if (doc.partidos) { emit(doc.partidos, doc); } }"
        }
    },
    "language": "javascript"
}

respuesta = requests.put(
    f"{URL_BASE}/{BASE_DATOS}/_design/losjugadores",
    headers={"Content-Type": "application/json"},
    json=design_doc
)

if respuesta.status_code in [201, 202]:
    print("Vistas creadas correctamente")
else:
    print("Estado creación de vistas:", respuesta.status_code)
    print(respuesta.text)
