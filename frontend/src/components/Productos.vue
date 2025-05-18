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
            <button @click="cambiarStock(producto.id, -1)" class="accion eliminar">➖</button>
            <button @click="cambiarStock(producto.id, 1)" class="accion agregar">➕</button>
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
            <button @click="cambiarStock(producto.id, 1)" class="accion agregar">➕</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { reactive, watch, onMounted } from 'vue'
import '../styles/productos.css'

// Lista principal de productos cargados desde el backend
const productos = reactive([])

// Listas separadas para los productos según disponibilidad
const disponibles = reactive([])
const noDisponibles = reactive([])

// Esta función actualiza las dos listas en base al estado actual
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

// Carga inicial de productos con una consulta GraphQL
function cargarProductos() {
  const query = `
    query {
      productos {
        id
        nombre
        precio
        stock
        disponible
      }
    }
  `
  fetch("http://localhost:5000/graphql", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  })
    .then(res => res.json())
    .then(data => {
      productos.splice(0)
      productos.push(...data.data.productos)
      actualizarListas()
    })
    .catch(err => console.error("Error cargando productos:", err))
}

// Realiza una mutación para cambiar el stock de un producto
function cambiarStock(id, cantidad) {
  const mutation = `
    mutation {
      modificarStock(id: ${id}, cantidad: ${cantidad}) {
        producto {
          id
          stock
          disponible
        }
      }
    }
  `
  fetch("http://localhost:5000/graphql", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: mutation })
  })
    .then(res => res.json())
    .then(result => {
      const actualizado = result.data.modificarStock.producto
      const index = productos.findIndex(p => p.id === actualizado.id)
      if (index !== -1) {
        productos[index].stock = actualizado.stock
        productos[index].disponible = actualizado.disponible
        actualizarListas()
      }
    })
    .catch(err => console.error("Error en la mutación:", err))
}

// Reactividad: si cambia productos, actualiza las listas
watch(productos, actualizarListas, { deep: true })

// Al cargar el componente, obtenemos los productos
onMounted(cargarProductos)
</script>
