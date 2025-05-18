1) ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

GraphQl permite consultar el campo necesario, para nuestra situacion es util al obtener "id","nombre" o "stock" sin recibir informacion extra o innecesaria.
Con una sola peticion se pueden recuperar todos los productos o hacer mutaciones. Esto simplifica el frontend.
Es mas flexible que REST porque con vistas a actualizxaciones futuras no hace falta crear nuevas rutas, solo ajustar las consultas.

2) ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
Los tipos y resolvers en una API GraphQL se definen a través del lenguaje del servidor que se esté usando.
Generalmente, se crean clases o estructuras que representan los tipos de datos, en nuestro caso producto, y luego se asociamos las funciones llamadas resolvers para indicar cómo obtener o modificar esos datos.
En la resolucion de la practica he utilizado la librería Graphene para Python. Definí una clase llamada "ProductoType" que representa un producto con los campos "id", "nombre", "precio", "stock" y "disponible", todos declarados usando los tipos de GraphQL

3) ¿Por qué es importante que el backend también actualice "disponible" y no depender solo del frontend?
En proyectos donde se divide front y back es importante centrar la logica en el backend, es una buena práctica mantener las reglas de negocio en el servidor para evitar errores o inconsistencias.
Si el front controlara ese campo los datos no serian coherentes si se consultase la API u otra interfaz

4) ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?
He implementado una función dentro de la mutación que se encarga de modificar el stock y actualizar automáticamente el campo "disponible". Esta lógica está incluida dentro del método "mutate", por lo que se aplica siempre que se hace una mutación desde el frontend o desde la interfaz de la APi.
Asi, no hay manera de modificar el stock sin que también se revise si el producto sigue estando disponible o no, garantizando que los datos se mantengan consistentes sin depender del cliente, y que la disponibilidad de cada producto esté con su stock real.

