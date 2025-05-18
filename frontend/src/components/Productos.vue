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
        <tr v-for="producto in disponibles" :key="producto.id">
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
        <tr v-for="producto in noDisponibles" :key="producto.id">
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
import { reactive, watch } from 'vue'
import '../styles/productos.css'

// Lista principal con los productos iniciales
const productos = reactive([
  { id: 1, nombre: 'Camiseta', precio: 20, stock: 3, disponible: true },
  { id: 2, nombre: 'Pantalón', precio: 30, stock: 0, disponible: false },
  { id: 3, nombre: 'Sudadera', precio: 50, stock: 2, disponible: true }
])

// Listas separadas para mostrar en cada tabla
const disponibles = reactive([])
const noDisponibles = reactive([])

// Lógica para repartir productos en las listas según su disponibilidad
function actualizarListas() {
  disponibles.length = 0
  noDisponibles.length = 0

  productos.forEach(p => {
    if (p.disponible) {
      disponibles.push(p)
    } else {
      noDisponibles.push(p)
    }
  })
}

// Reactivo para cada producto
productos.forEach(producto => {
  watch(
    () => producto.stock,
    (nuevo) => {
      producto.disponible = nuevo > 0
      actualizarListas()
    }
  )
})

// Aumentar el stock
function agregarStock(producto) {
  producto.stock++
}

// Reducir el stock
function quitarStock(producto) {
  if (producto.stock > 0) {
    producto.stock--
  }
}

// Inicializar las listas
actualizarListas()
</script>