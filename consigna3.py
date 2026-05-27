m = [
    [120, 150, 100],
    [200, 180, 220],
    [90,  110,  95]
]

print("Tiempo promedio de ejecución por funcion")
for i in range(3):
    suma_fila = 0
    for j in range(3):
        suma_fila = suma_fila + m[i][j]
    promedio = suma_fila // 3
    print("Funcion", i, promedio, "ms")

print("Tiempo promedio de ejecución por servidor")
for j in range(3):
    suma_columna = 0
    for i in range(3):
        suma_columna = suma_columna + m[i][j]
    promedio = suma_columna // 3
    print("Servidor", j, promedio, "ms")

print("Matriz Transpuesta M^T:")
for j in range(3):
    fila_transpuesta = [0, 0, 0]
    for i in range(3):
        fila_transpuesta[i] = m[i][j]
    print(fila_transpuesta)
