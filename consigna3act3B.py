def cargar_matriz():
    matriz_local = []
    for servidor in range(2):
        fila_servidor = []
        for funcion in range(3):
            num = int(input("Ingrese un numero: "))
            fila_servidor.append(num)
        matriz_local.append(fila_servidor)
    return matriz_local

def mostrar_matriz(M):
    print("Matriz:")
    for fila in M:
        print(fila)

def promedio_por_funcion(M):
    print("\nPromedio por funcion:")

    for funcion in range(3):
        suma = 0
    
        for servidor in range(2):
            suma = suma + M[servidor][funcion]
        
        promedio = suma / 2
        print(promedio)

def promedio_por_servidor(M):
    print("\nPromedio por servidor:")

    for servidor in range(2):
        suma = 0

        for funcion in range(3):
            suma = suma + M[servidor][funcion]
            
        promedio = suma / 3
        print(promedio)