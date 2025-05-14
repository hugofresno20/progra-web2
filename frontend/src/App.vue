<template>
  <div class="container">
    <h1>Concesionario Santander</h1>

    <div class="productos">
      <div class="card" v-for="(producto, index) in productos" :key="index">
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
          <button class="comprar" @click="incrementarStock(index)">+ COMPRAR</button>
          <button class="vender" @click="reducirStock(index)" :disabled="producto.stock === 0">- VENDER</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'

const productos = reactive([
  { nombre: 'Ferrari LaFerrari', precio: 500000, stock: 2, disponible: true },
  { nombre: 'Mercedes a45 AMG', precio: 100000, stock: 7, disponible: true },
  { nombre: 'BMW M4', precio: 130000, stock: 5, disponible: true },
  { nombre: 'Ford Focus ST', precio: 40000, stock: 15, disponible: true },
  { nombre: 'Tesla Model S', precio: 100000, stock: 3, disponible: true },
  { nombre: 'Honda Civic Type R', precio: 65000, stock: 5, disponible: true }
])

function incrementarStock(index) {
  productos[index].stock++
}

function reducirStock(index) {
  if (productos[index].stock > 0) {
    productos[index].stock--
  }
}

productos.forEach((producto) => {
  watch(
      () => producto.stock,
      (nuevoStock) => {
        producto.disponible = nuevoStock > 0
      }
  )
})
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
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #2c3e50;
}

.productos {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.card {
  background-color: #f4f4f4;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  width: 280px;
  text-align: left;
}

.card h3 {
  margin-top: 0;
  color: #333;
}

.card p {
  margin: 0.5rem 0;
}

.disponible {
  color: green;
  font-weight: bold;
}

.no-disponible {
  color: red;
  font-weight: bold;
}

.botones {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button.comprar {
  background-color: #d1fae5;
}

button.comprar:hover {
  background-color: #a7f3d0;
}

button.vender {
  background-color: #fee2e2;
}

button.vender:hover {
  background-color: #fecaca;
}

button:disabled {
  background-color: #e5e7eb;
  cursor: not-allowed;
}
</style>
