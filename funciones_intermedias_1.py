# funciones_intermedias_1.py
# Ejercicios intermedios con diccionarios y funciones en Python

# 1. Actualizar valores en diccionarios y listas
print("\n--- Ejercicio 1: Actualizar valores ---")

# Estructuras de datos iniciales
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]

# Actualizaciones solicitadas
matriz[1][0] = 6  # Cambia el 3 por 6 en la matriz
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Actualiza nombre del cantante
ciudades["México"][2] = "Monterrey"  # Reemplaza "Cancún" por "Monterrey"
coordenadas[0]["latitud"] = 9.9355431  # Actualiza latitud

# Verificaciones
print("Matriz actualizada:", matriz)
print("Primer cantante:", cantantes[0]["nombre"])
print("Ciudades de México:", ciudades["México"])
print("Nueva latitud:", coordenadas[0]["latitud"])


# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    print("\n--- Ejercicio 2: Iterar diccionarios ---")
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}", end=", " if llave != list(diccionario.keys())[-1] else "\n")
        # Alternativa BONUS (comentar la línea anterior y descomentar esta):
        # print(", ".join([f"{llave} - {valor}" for llave, valor in diccionario.items()]))

# Ejemplo de uso
cantantes_ejemplo = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes_ejemplo)

# -------------------------------------------------------------------
# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    print("\n--- Ejercicio 3: Valores por llave ---")
    for diccionario in lista:
        print(diccionario.get(llave, "Llave no encontrada"))

# Ejemplo de uso
iterarDiccionario2("nombre", cantantes_ejemplo)
iterarDiccionario2("pais", cantantes_ejemplo)

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    print("\n--- Ejercicio 4: Diccionario con listas ---")
    for llave, valores in diccionario.items():
        print(f"{len(valores)} {llave.upper()}")
        for valor in valores:
            print(valor)
        print()  # Espacio entre secciones

# Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformacion(costa_rica)