import requests
import json
from credenciales import USUARIO, PASSWORD, HOST, PUERTO

URL_BASE = f"http://{USUARIO}:{PASSWORD}@{HOST}:{PUERTO}"
BASE_DATOS = "jugadores"

# 1. Crear la base de datos jugadores
respuesta = requests.put(f"{URL_BASE}/{BASE_DATOS}")

if respuesta.status_code == 201:
    print("Base de datos jugadores creada correctamente")
elif respuesta.status_code == 412:
    print("La base de datos jugadores ya existe")
else:
    print("Error creando la base de datos:", respuesta.text)

# 2. Leer el archivo JSON generado
with open("mundial_2026.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# 3. Cargar documentos a CouchDB con _bulk_docs
respuesta = requests.post(
    f"{URL_BASE}/{BASE_DATOS}/_bulk_docs",
    headers={"Content-Type": "application/json"},
    json=datos
)

print("Estado:", respuesta.status_code)
print(respuesta.json())
