# Proyecto Tienda Online — Programación Web
Este repositorio contiene el desarrollo realizado por Sergio Velarde para dar solucion a las practicas propuestas en la asignatura programacion web 2.
La solucion da vida a la gestion de stock de una tienda online. Esta organizado en ramas y carpetas separadas para facilitar su revision.

No realicé la entrega de la práctica 1 en su momento y pido perdon ya que no recordé la entrega y estos dias revisando los correos vi las dos tareas. 
Entiendo que esto pueda suponer una falta a la hora de calificar el apartado de la practica1 pero espero que se tenga en consideracion la entrega.
Perdonen las molestias.


## Estructura general
```
prograWeb/
├── frontend/ # Aplicación Vue.js  Práctica 1
├── backend/ # Servidor Flask + GraphQL desarrollado en la Práctica 2
├── README.md # Este archivo
```

## Práctica 1 — Frontend
En esta primera parte se desarrolló una interfaz en Vue que muestra una lista de productos disponibles y no disponibles, controlando su visibilidad según el stock.  
La lógica de reactividad se implementó con `reactive()` y `watch()`, sin usar `computed`, tal como pedía el enunciado.

Respuestas a las preguntas solicitadas: `frontend/Respuestas.md`
Rama de desarrollo: `front-dev`    
Rama asociada para probar la funcionalidad: `front-practica1`


## Práctica 2 — Backend
En esta segunda práctica se implementó un backend con Flask y GraphQL. Los productos se almacenan en memoria y se puede modificar su stock a través de una API.  
El campo `disponible` se actualiza automáticamente en el servidor, sin depender del frontend.
Para el desarrollo de esta practica tambien se modifico el archivo producto.vue del frontend para que trabajase con el backend.

Respuestas a las preguntas solicitadas: `backend/Respuestas.md`    
Rama de desarrollo: `backend-dev`  
Rama final fusionada y funcional: `main`

## Las instrucciones para el funcionamiento de cada apartado se encuentran en sus respectivos directorios en los archivos README