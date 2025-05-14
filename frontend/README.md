# Tienda Reactiva - Concesionario Santander 

Este concesionario de coches es una tienda online simulada desarrollada con **Vue 3** y **Vite**.

##  Requisitos implementados

- Cada producto tiene: `nombre`, `precio`, `stock`, `disponible`.
- Cuando el stock de un producto baja a 0, `disponible` pasa automáticamente a `false` mientras tanto permanece en `true`.
- La interfaz muestra qué productos están disponibles y cuáles no.

---

##  Preguntas teóricas

### 1. Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?

Cuando usás reactive() en Vue, hay que tener en cuenta que no estará atento automáticamente a los cambios dentro de los objetos, como por ejemplo una propiedad específica de un producto.

Entonces, para que Vue reaccione cuando cambia `producto.stock`, hay que decírselo explícitamente usando `watch()` y pasándole una función que devuelva justo esa propiedad:

```js
watch(() => producto.stock, (nuevoStock) => {
  producto.disponible = nuevoStock > 0
})
```
De esta forma, cada vez que cambia el stock, Vue ejecuta la función que está dentro del watch() y actualiza el campo disponible automáticamente.

### 2. watch() permite escuchar cambios en propiedades específicas dentro de reactive(), explica cómo funciona.
watch() sirve para escuchar cuando cambia algo y ejecutar una función en ese momento.

Cuando usamos reactive() para tener datos reactivos (como una lista de productos), podemos usar watch() para mirar una propiedad específica y reaccionar si cambia.

```js
watch(
  () => producto.stock,        // esto le dice a Vue qué propiedad mirar
  (nuevo, viejo) => {          // esta es la función que se ejecuta si cambia
    console.log('Stock cambió:', viejo, '→', nuevo)
  }
)
```

O sea, le pasás dos cosas:

1. Una función que devuelva lo que quieres observar 

2. Una función que se va a ejecutar cada vez que eso cambie

Esto lo usamos para, por ejemplo, cambiar automáticamente `producto.disponible` según el stock, sin tener que hacerlo manualmente todo el tiempo.

### 3. ¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?
Cuando tienes un array de objetos con reactive() (como una lista de productos), Vue no puede "mirar" todos los stock automáticamente.

Entonces, lo que hay que hacer es recorrer el array y ponerle un watch() a cada producto individualmente, observando la propiedad `stock`.

```js
productos.forEach((producto) => {
    watch(
        () => producto.stock,
        (nuevoStock) => {
            producto.disponible = nuevoStock > 0
        }
    )
})
```
De esta forma, cada vez que cambia el stock de un producto, se actualiza también su `disponible`.
