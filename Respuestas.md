
##  Preguntas teóricas

### 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?
La principal ventaja es que `GraphQL` permite pedir solo los datos que necesitas. En este proyecto, por ejemplo, desde el frontend podemos pedir solo el `nombre`, el `precio` o el `stock` sin que el servidor tenga que mandarnos todo el objeto completo cada vez.
También es más cómodo porque con una sola petición podemos hacer varias cosas a la vez. Por ejemplo, consultar todos los productos o hacer una modificación, sin tener que crear rutas distintas como en REST. Todo va por una única URL.

---

### 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
En este caso usamos graphene en Python. Primero se crea una clase que representa el tipo de dato, por ejemplo Producto, donde se definen los campos como `id`, `nombre`, `precio`, etc.
Luego, los resolvers son las funciones que devuelven los datos. Por ejemplo, el resolver de productos devuelve la lista que tenemos guardada en memoria. 
En las mutaciones también hay funciones que se encargan de aplicar cambios, como cuando se modifica el `stock` de un producto.

---

### 3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?
Porque si solo lo actualizáramos en el frontend, los datos estarían bien solo ahí, pero en el backend seguiría estando mal. Eso podría causar errores si se consulta la API desde otro sitio, como Postman o una app móvil.
Además, cualquier cambio de `stock` debe ir siempre acompañado de un cambio en disponible, y eso es responsabilidad del backend. Así nos aseguramos de que la lógica sea siempre la misma, sin importar desde dónde se use.

---

### 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
Toda la lógica está dentro de la mutación `modificarStock`, en el backend. Ahí se comprueba que si el `stock` llega a 0, el producto pasa a no estar disponible. Y si vuelve a subir, se activa otra vez.
Además, he hecho un pequeño archivo `test.py` que hace estas pruebas automáticamente. Así me aseguro de que esa lógica funciona bien y no depende del navegador ni del frontend para aplicarse.
