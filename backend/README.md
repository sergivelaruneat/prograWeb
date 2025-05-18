# Backend de la Tienda Online con Flask + GraphQL
Este módulo implementa el backend de una tienda online utilizando Flask y GraphQL. Permite consultar y modificar productos en memoria, cumpliendo con los requisitos académicos de la práctica.

## Estructura del directorio
```
backend/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── schema.py
│ └── data.py
├── venv/ # Entorno virtual
├── run.py # Punto de entrada del servidor Flask
├── requirements.txt # Dependencias necesarias
└── README.md Usted esta aqui :)
```

## Requisitos
- Python 3.11 o superior
- Git (para clonar el repositorio)
- Entorno virtual activado antes de ejecutar cualquier comando

## Levantar el backend
### 1. Accede al directorio del backend
```bash
cd backend
```

### 2. Crea el entorno virtual, esto solo hacerlo la primera vez
```bash
python -m venv venv
```

### 3. Activa el entorno virtual
```bash
.\venv\Scripts\Activate.ps1
```

### 4. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecuta el servidor
```bash
python run.py
```

# Informacion adiccional
Si todo esta correcto el servidor estara corriendo en el puerto indicado por un mensaje
Recuerde que para entrar a la interfaz grafica debera entrar en /graphql
http://localhost:5000/graphql

# Puerbas test.py
Asegúrate de tener el backend en marcha:
```bash
python run.py
```

En otra terminal con el entorno activado, ejecuta:
```bash
python test.py
```

Si las pruebas son correctas mostrara el siguiente mensaje:
```bash
Consulta de productos OK
Mutación y lógica de disponible OK
```
