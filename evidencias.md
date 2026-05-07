## Cómo replicar el proyecto en otra computadora

### 1. Clonar el repositorio

```bash
git clone https://github.com/PlataformasWeb-P-AA2026/taller05-team-5.git
cd taller05-team-2
```

---

### 2. Generar el archivo JSON (solo si no existe)

⚠️ Este paso se realiza **únicamente si no se dispone del archivo `mundial_2026.json`**.

Ingresar a la carpeta:

```bash
cd formato-json
```

Instalar librerías necesarias:

```bash
pip install beautifulsoup4 pypdf
```

Ejecutar el script:

```bash
python generar_json.py
```

Esto generará el archivo:

```text
mundial_2026.json
```

---

### 3. Cargar datos en CouchDB

Instalar librería adicional:

```bash
pip install requests
```

Ejecutar el script:

```bash
python cargar_couchdb.py
```

Esto creará automáticamente la base de datos:

```text
jugadores
```

y cargará los datos desde `mundial_2026.json`.

---

### 4. Ejecutar el frontend

Regresar a la raíz del proyecto:

```bash
cd ..
```

Ingresar a la carpeta frontend:

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

Ejecutar la aplicación:

```bash
npm run dev
```

Abrir en el navegador:

```text
http://localhost:5173
```

---

###  Resultado esperado

- Base de datos `jugadores` creada en CouchDB  
- Datos cargados correctamente  
- Vistas funcionando  
- Frontend mostrando los datos

## Evidencia de carga en CouchDB 

<img width="1600" height="957" alt="WhatsApp Image 2026-05-07 at 11 42 16 AM" src="https://github.com/user-attachments/assets/d349c4cb-da9a-4aef-b9ac-5290b9a8dd17" />
<img width="1600" height="559" alt="WhatsApp Image 2026-05-07 at 11 42 42 AM" src="https://github.com/user-attachments/assets/02ed30e2-353d-4fc0-a6ae-7a727b19fb7a" />

## Capturas del frontend funcionando 
<img width="1600" height="922" alt="WhatsApp Image 2026-05-07 at 11 54 08 AM" src="https://github.com/user-attachments/assets/b0245cb3-3eba-442b-9e10-f7c83326fa86" />

<img width="1600" height="998" alt="WhatsApp Image 2026-05-07 at 11 58 25 AM" src="https://github.com/user-attachments/assets/7bf89e42-52bb-43c1-8b53-b8ca75913e04" />
