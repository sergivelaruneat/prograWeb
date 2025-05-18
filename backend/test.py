import requests

# URL base de la API
URL = "http://localhost:5000/graphql"

# Función con consulta simple
def test_consulta_productos():
    query = """
    query {
        productos {
            id
            nombre
            stock
            disponible
        }
    }
    """
    respuesta = requests.post(URL, json={"query": query})
    datos = respuesta.json()

    # Comprobamos que la respuesta contiene los datos esperados
    assert "data" in datos
    assert "productos" in datos["data"]
    print("✅ Consulta de productos OK")

# Función que prueba la mutación de stock y la lógica de disponibilidad
def test_mutacion_stock_y_disponible():
    mutation = """
    mutation {
        modificarStock(id: 1, cantidad: -100) {
            producto {
                id
                stock
                disponible
            }
        }
    }
    """
    respuesta = requests.post(URL, json={"query": mutation})
    datos = respuesta.json()
    producto = datos["data"]["modificarStock"]["producto"]

    # Esperamos que el stock sea 0 y que el producto no esté disponible
    assert producto["stock"] == 0
    assert producto["disponible"] == False
    print("✅ Mutación y lógica de disponible OK")

# Llamadas a las funciones cuando se ejecuta el archivo
if __name__ == "__main__":
    test_consulta_productos()
    test_mutacion_stock_y_disponible()
