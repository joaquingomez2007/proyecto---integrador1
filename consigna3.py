# Definimos la matriz M
M = [
    [120, 150, 100],  # Función 0
    [200, 180, 220],  # Función 1
    [90, 110, 95]     # Función 2
]

print("--- Tiempo promedio de ejecución por función ---")

for i in range(3):
    suma_funcion = 0
    for j in range(3):
        suma_funcion += M[i][j]
        
    promedio = suma_funcion // 3 
    print("Función", i, ":", promedio, "ms")


print("\n--- Tiempo promedio de ejecución por servidor ---")

for j in range(3):
    suma_servidor = 0
    for i in range(3):
        suma_servidor += M[i][j]
        
    promedio = suma_servidor // 3  
    print("Servidor", j, ":", promedio, "ms")

M_transpuesta =[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(3):
    for j in range(3):
        M_transpuesta[j][i] = M[i][j]

for fila in M_transpuesta:
    print(fila)