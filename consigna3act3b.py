# Matriz de tiempos
M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

# Promedio por funcion
print("Promedio por funcion:")

for fila in range(3):
    suma = 0

    for columna in range(3):
        suma = suma + M[fila][columna]

    promedio = suma / 3

    print("Funcion", fila + 1, ":", promedio)

# Promedio por servidor
print("\nPromedio por servidor:")

for columna in range(3):
    suma = 0

    for fila in range(3):
        suma = suma + M[fila][columna]

    promedio = suma / 3

    print("Servidor", columna + 1, ":", promedio)

print("\nMatriz transpuesta:")

for columna in range(3):
    for fila in range(3):
        print(M[fila][columna], end=" ")
    print()
