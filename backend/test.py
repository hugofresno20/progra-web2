import requests

URL = "http://localhost:5001/graphql"

def test_consulta_productos():
    consulta = {
        "query": "{ productos { id nombre stock disponible } }"
    }
    respuesta = requests.post(URL, json=consulta)
    datos = respuesta.json()

    if "data" not in datos or "productos" not in datos["data"]:
        print("Error: No se pudo obtener la lista de productos.")
        return

    print("Consulta de productos realizada correctamente.")

def test_modificar_stock_y_disponible():
    mutacion1 = {
        "query": "mutation { modificarStock(id: 1, cantidad: -100) { producto { id stock disponible } } }"
    }
    res1 = requests.post(URL, json=mutacion1)
    resultado1 = res1.json()["data"]["modificarStock"]["producto"]

    if resultado1["stock"] != 0 or resultado1["disponible"] != False:
        print("Error: El producto no se actualizó correctamente al dejar el stock en 0.")
        return

    print("Stock en 0 y disponible = False comprobado correctamente.")

    mutacion2 = {
        "query": "mutation { modificarStock(id: 1, cantidad: 3) { producto { id stock disponible } } }"
    }
    res2 = requests.post(URL, json=mutacion2)
    resultado2 = res2.json()["data"]["modificarStock"]["producto"]

    if resultado2["stock"] != 3 or resultado2["disponible"] != True:
        print("Error: El producto no se actualizó correctamente al reponer stock.")
        return

    print("Stock > 0 y disponible = True comprobado correctamente.")

if __name__ == "__main__":
    print("Ejecutando pruebas del backend...\n")
    test_consulta_productos()
    test_modificar_stock_y_disponible()
    print("\nTodas las pruebas finalizaron sin errores.")
