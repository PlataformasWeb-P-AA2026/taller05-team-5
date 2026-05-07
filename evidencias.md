## Cómo replicar el proyecto en otra computadora

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd taller05-team-2
```

---

### 2. Generar el archivo JSON (solo si no existe)

⚠️ Este paso se realiza **únicamente si no se dispone del archivo `mundial_2026.json`**.

Ingresar a la carpeta:

```bash
cd formato-json
```

### Activar entorno de Python (si aplica)

En Windows:

```bash
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
source venv/bin/activate
```

*(Este paso es necesario si se está usando un entorno virtual)*

---

### Instalar librerías

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

---

### 3.Cargar datos en CouchDB

Instalar librería adicional:

```bash
pip install requests
```

Ejecutar:

```bash
python cargar_couchdb.py
```

Esto creará automáticamente la base de datos:

```text
jugadores
```

y cargará los datos.

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
- Datos cargados correctamente  
- Vistas funcionando  
- Frontend mostrando los datos  
