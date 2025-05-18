# Tienda Reactiva - Concesionario Santander 

Este proyecto es una tienda online de coches hecha con **Vue 3** en el frontend y **Flask + GraphQL** en el backend. Permite ver los productos disponibles, su stock y modificarlo en tiempo real.

## Tecnologías usadas

- Vue 3 + Vite
- Flask
- Graphene (GraphQL para Python)
- fetch() para conectar frontend y backend
- flask-cors para evitar errores de CORS

##  Requisitos implementados

- Cada producto tiene: `id`, `nombre`, `precio`, `stock`, y `disponible`.
- El stock se puede aumentar o reducir desde la interfaz.
- Si el stock baja a 0, el producto pasa automáticamente a **no disponible**.
- Si el stock vuelve a subir, pasa de nuevo a **disponible**.
- Toda esta lógica se aplica en el **backend**, no en el frontend.

---

## Cómo iniciar 

### Backend


```bash
cd backend #Acceder a la carpeta 
source venv/bin/activate #Activar el entorno virtual
pip install flask graphene flask-cors #Instalar dependeicas
python app.py #Ejecutar el backend

```
 · El backend quedara inicializado en la siguiente ruta:
 #### http://localhost:5001/graphql
---

## Frontend 


```bash
cd frontend
npm install #Descarga lo necesario para que funcione vue
npm run dev #Inicializa el front
```
 · El frontend quedara inicializado en la siguiente ruta:
 #### http://localhost:5173

---

## Como probar el test

El archivo `test.py`:

- Si se puede consultar correctamente la lista de productos.
- Si el stock y la propiedad `disponible` se actualizan correctamente en el backend.

Para ejecutar:

```bash
cd backend #Accede a la carpeta del backend
source venv/bin/activate #Activar el entorno virtual
python test.py #Ejecuta archivo de test
```
