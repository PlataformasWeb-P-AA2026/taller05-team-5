import csv
import json
from bs4 import BeautifulSoup
from pypdf import PdfReader

docs = []

# 1. Leer HTML - Europa
with open("../data/fuente_html_europa.html", "r", encoding="utf-8") as archivo:
    soup = BeautifulSoup(archivo, "html.parser")

filas = soup.find_all("tr")[1:]

for fila in filas:
    celdas = fila.find_all("td")

    docs.append({
        "nombre": celdas[0].text,
        "seleccion": celdas[1].text,
        "posicion": celdas[2].text,
        "edad": int(celdas[3].text),
        "club_actual": celdas[4].text,
        "fuente": "HTML Europa"
    })


# 2. Leer CSV - Sudamérica
with open("../data/fuente_csv_sudamerica.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        docs.append({
            "nombre": fila["nombre"],
            "seleccion": fila["seleccion"],
            "posicion": fila["posicion"],
            "edad": int(fila["edad"]),
            "partidos": int(fila["partidos"]),
            "fuente": "CSV Sudamérica"
        })


# 3. Leer PDF - Norteamérica y Asia
reader = PdfReader("../data/fuente_pdf_norteamerica_asia.pdf")

texto = ""
for pagina in reader.pages:
    texto += pagina.extract_text() + "\n"

lineas = [linea.strip() for linea in texto.splitlines() if linea.strip()]

datos = lineas[5:]

for i in range(0, len(datos), 5):
    docs.append({
        "nombre": datos[i],
        "seleccion": datos[i + 1],
        "posicion": datos[i + 2],
        "edad": int(datos[i + 3]),
        "goles": int(datos[i + 4]),
        "fuente": "PDF Norteamérica Asia"
    })


# Formato requerido por CouchDB
salida = {
    "docs": docs
}

with open("mundial_2026.json", "w", encoding="utf-8") as archivo:
    json.dump(salida, archivo, indent=4, ensure_ascii=False)

print("Archivo mundial_2026.json generado correctamente")
print("Total de jugadores:", len(docs))
