# Crear matriz vacía de 3x3
matriz = [[0] * 3 for i in range(3)]

# Cargar valores
print("Ingrese los valores de la matriz:")

for i in range(3):          # filas
    for j in range(3):      # columnas
        matriz[i][j] = int(input(f"Elemento [{i}][{j}]: "))

# Mostrar matriz
print("\nMatriz ingresada:")

for i in range(3):          # filas
    for j in range(3):      # columnas
        print(matriz[i][j], end=" ")
    print()