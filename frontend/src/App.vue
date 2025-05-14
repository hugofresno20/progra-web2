<template>
  <div class="container">
    <h1>Concesionario Santander</h1>

    <div class="productos">
      <div class="card" v-for="(producto, index) in productos" :key="producto.id">
        <h3>{{ producto.nombre }}</h3>
        <p>Precio: <strong>${{ producto.precio }}</strong></p>
        <p>Stock: {{ producto.stock }}</p>
        <p>
          Disponible:
          <span :class="producto.disponible ? 'disponible' : 'no-disponible'">
            {{ producto.disponible ? 'Sí' : 'No' }}
          </span>
        </p>

        <div class="botones">
          <button class="comprar" @click="incrementarStock(producto.id)">+ COMPRAR</button>
          <button class="vender" @click="reducirStock(producto.id)" :disabled="producto.stock === 0">- VENDER</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, onMounted } from 'vue'

const productos = reactive([])

onMounted(() => {
  fetch('http://localhost:5001/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        {
          productos {
            id
            nombre
            precio
            stock
            disponible
          }
        }
      `
    })
  })
    .then(res => res.json())
    .then(data => {
      productos.splice(0, productos.length, ...data.data.productos)
    })
    .catch(err => {
      console.error('Error al cargar productos:', err)
    })
})

function modificarStock(id, cantidad) {
  fetch('http://localhost:5001/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        mutation {
          modificarStock(id: ${id}, cantidad: ${cantidad}) {
            producto {
              id
              nombre
              precio
              stock
              disponible
            }
          }
        }
      `
    })
  })
    .then(res => res.json())
    .then(data => {
      const actualizado = data.data.modificarStock.producto
      const index = productos.findIndex(p => p.id === actualizado.id)
      if (index !== -1) {
        productos[index] = actualizado
      }
    })
    .catch(err => {
      console.error('Error al modificar stock:', err)
    })
}

function incrementarStock(id) {
  modificarStock(id, 1)
}

function reducirStock(id) {
  modificarStock(id, -1)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

/* ... (tu estilo está perfecto, no cambia nada) ... */
</style>
