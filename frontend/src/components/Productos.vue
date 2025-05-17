<template>
  <div class="contenedor">
    <h2>Productos Disponibles</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productosDisponibles" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>${{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>
            <button @click="quitarStock(producto)" class="accion eliminar">➖</button>
            <button @click="agregarStock(producto)" class="accion agregar">➕</button>
          </td>
        </tr>
      </tbody>
    </table>

    <h2>Productos No Disponibles</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productosNoDisponibles" :key="producto.id">
          <td>{{ producto.id }}</td>
          <td>{{ producto.nombre }}</td>
          <td>${{ producto.precio }}</td>
          <td>{{ producto.stock }}</td>
          <td>
            <button @click="agregarStock(producto)" class="accion agregar">➕</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { reactive, watch, computed, onMounted } from 'vue'
import '../styles/productos.css'

const productos = reactive([
  { id: 1, nombre: 'Camiseta', precio: 20, stock: 3, disponible: true },
  { id: 2, nombre: 'Pantalón', precio: 30, stock: 0, disponible: false },
  { id: 3, nombre: 'Sudadera', precio: 50, stock: 2, disponible: true }
])

productos.forEach(producto => {
  watch(
    () => producto.stock,
    (nuevoStock) => {
      producto.disponible = nuevoStock > 0
    }
  )
})

const productosDisponibles = computed(() =>
  productos.filter(p => p.disponible)
)

const productosNoDisponibles = computed(() =>
  productos.filter(p => !p.disponible)
)

const agregarStock = (producto) => {
  producto.stock++
}

const quitarStock = (producto) => {
  if (producto.stock > 0) producto.stock--
}
</script>
