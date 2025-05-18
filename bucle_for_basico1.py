# bucle_for_basico1.py
# Ejercicios básicos con bucles for en Python

# 1. Básico: imprime todos los números enteros del 0 al 100.
print("\n--- Ejercicio 1: Básico ---")
for numero in range(101):  # range(101) genera números del 0 al 100
    print(numero)

# 2. Múltiples de 2: imprime todos los múltiplos de 2 entre 2 y 500.
print("\n--- Ejercicio 2: Múltiples de 2 ---")
for numero in range(2, 501, 2):  # Empieza en 2, termina en 500, avanza de 2 en 2
    print(numero)

# 3. Contando Vanilla Ice: imprime números del 1 al 100, con reglas especiales.
print("\n--- Ejercicio 3: Contando Vanilla Ice ---")
for numero in range(1, 101):
    if numero % 10 == 0:  # Si es divisible por 10
        print("baby")
    elif numero % 5 == 0:  # Si es divisible por 5 (pero no por 10)
        print("ice ice")
    else:
        print(numero)

# 4. Wow. Número gigante a la vista: suma los pares del 0 al 500,000.
print("\n--- Ejercicio 4: Suma de pares (0-500,000) ---")
suma_pares = 0
for numero in range(0, 500001, 2):  # Avanzamos de 2 en 2 (solo pares)
    suma_pares += numero
print("La suma total es:", suma_pares)

# 5. Regrésame al 3: cuenta regresiva desde 2024, restando 3 cada vez.
print("\n--- Ejercicio 5: Regrésame al 3 ---")
for numero in range(2024, 0, -3):  # Inicia en 2024, termina antes de 0, resta 3
    print(numero)

# 6. Contador dinámico: imprime múltiplos entre numInicial y numFinal.
print("\n--- Ejercicio 6: Contador dinámico ---")
numInicial = int(input("Ingresa el número inicial: "))
numFinal = int(input("Ingresa el número final: "))
multiplo = int(input("Ingresa el múltiplo: "))

for numero in range(numInicial, numFinal + 1):  # Incluye numFinal
    if numero % multiplo == 0:  # Si es múltiplo del número dado
        print(numero)
