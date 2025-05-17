1) Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?
Cuando se usan estructuras como arrays de objetos, como la lista de productos con propiedades anidadas como stock, los cambios internos no se detectan automáticamente siempre.
Para detectar estos cambios, usamos un watch() con la opción {deep: true}. Esto le dice a Vue que observe el objeto en cualquier propiedad anidada, no solo en el objeto raíz y sus propiedades internas. Aqui es cuandop producimos el cambio al reducir el stock y esta caracteristica lo detecta. 
Esta es la linea: watch(productos, actualizarListas, { deep: true })

2) watch() permite escuchar cambios en propiedades específicas dentro de reactive(). Explica cómo funciona.
watch() es una función que permite reaccionar a los cambios de una o varias propiedades. Cuando lo usamos con un objeto creado con reactive(), puedes pasarle el objeto completo como primer argumento y añadir { deep: true } para que Vue escuche cambios en propiedades internas.
watch() observa el valor que le pases como primer argumento (una referencia o función). Cuando ese valor cambia, ejecuta el callback. 

3) ¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?
Dado que stock es una propiedad interna de cada objeto en un array, necesitas observar el array completo con deep: true
Esto asegura que cada vez que cambia el stock de un producto, la lógica de disponibilidad se ejecute y se actualice correctamente.