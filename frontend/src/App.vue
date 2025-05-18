<template>
  <div class="container">
    <h1>Concesionario Santander graphql</h1>

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
          <button class="vender" @click="reducirStock(producto.id)" :disabled="producto.stock === 0">- VENDER</button>
          <button class="comprar" @click="incrementarStock(producto.id)">+ COMPRAR</button>
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

.container {
  font-family: 'Inter', sans-serif;
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #1f2937;
}

.productos {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
}

.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  width: 260px;
  padding: 1.5rem;
  transition: transform 0.2s ease;
  border: 1px solid #e5e7eb;
}

.card:hover {
  transform: translateY(-4px);
}

.card h3 {
  margin-top: 0;
  font-size: 1.2rem;
  color: #111827;
}

.card p {
  margin: 0.5rem 0;
  color: #374151;
  font-size: 0.95rem;
}

.disponible {
  color: #10b981;
  font-weight: bold;
}

.no-disponible {
  color: #ef4444;
  font-weight: bold;
}

.botones {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}

button {
  padding: 0.4rem 0.8rem;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

button.comprar {
  background-color: #d1fae5;
  color: #065f46;
}

button.comprar:hover {
  background-color: #a7f3d0;
}

button.vender {
  background-color: #fee2e2;
  color: #991b1b;
}

button.vender:hover {
  background-color: #fecaca;
}

button:disabled {
  background-color: #e5e7eb;
  color: #9ca3af;
  cursor: not-allowed;
}
</style>

