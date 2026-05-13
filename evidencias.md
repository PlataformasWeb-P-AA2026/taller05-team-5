## Cómo replicar el proyecto en otra computadora

### 1. Clonar el repositorio

```bash
git clone https://github.com/PlataformasWeb-P-AA2026/taller05-team-5.git
cd taller05-team-2
```

---

### 2. Generar el archivo JSON (solo si no existe)

⚠️ Este paso se realiza **únicamente si no se dispone del archivo `mundial_2026.json`**.

### Instalar librerías

Ingresar a la carpeta:

```bash
cd formato-json
```

### Activar entorno de Python 

En Windows:

```bash
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
source venv/bin/activate
```

```bash
pip install beautifulsoup4 pypdf
```

---

### Ejecutar script

```bash
python generar_json.py
```

Esto generará el archivo:

```text
mundial_2026.json
```
⚠️ hasta este punto llega el paso que **únicamente si no se dispone del archivo `mundial_2026.json`**.
---

### 3.Cargar datos en CouchDB

Ingresar a la carpeta:

```bash
cd formato-json
```

### Activar entorno de Python 

En Windows:

```bash
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
source venv/bin/activate
```
---

Instalar librería adicional:

```bash
pip install requests
```

Ejecutar:

```bash
python cargar_couchdb.py
```

Esto cargara automáticamente a la base de datos,antes debe generar la base de datos con el nombre jugadores en CouchDB:

```text
jugadores
```

---

### 4. Ejecutar el frontend

Regresar a la raíz:

```bash
cd ..
```

Entrar al frontend:

```bash
cd frontend
```

Seleccionar versión de Node (si aplica):

```bash
nvm use 22
```

Instalar dependencias:

```bash
npm install
```

Ejecutar:

```bash
npm run dev
```

Abrir en el navegador:

```text
http://localhost:5173
```

---

### Resultado esperado

- Base de datos `jugadores` creada en CouchDB
 <img width="1807" height="513" alt="image" src="https://github.com/user-attachments/assets/478467d3-6952-4d29-a3a6-8b4a705feaa4" />
 Datos cargados correctamente
- <img width="1600" height="957" alt="image" src="https://github.com/user-attachments/assets/dc60757f-ce19-4bfa-b89c-b24f008d4ce2" />
 Vistas funcionando
- <img width="1807" height="1056" alt="image" src="https://github.com/user-attachments/assets/e43793f7-0aaf-4bba-85e5-977777504979" />
- Frontend mostrando los datos
 <img width="1600" height="998" alt="image" src="https://github.com/user-attachments/assets/5cf280c6-1d97-4516-ac1e-3aef55d38683" />
  



