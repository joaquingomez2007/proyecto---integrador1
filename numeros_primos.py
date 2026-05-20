n = int(input('ingrese un numero: '))
es_primo = True
if n < 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break 
if es_primo:
    print('el numero es primo')
else:    
    print('el numero no es primo')
for i in range(1, 11):
    print(n, '*', i, '=', n * i)
cantidad = int(input('ingrese la cantidad de numeros que desea: '))
menor = None
for i in range(cantidad):
    numero = int(input('ingrese un numero: '))
    if menor is None or numero < menor:
        menor = numero
print('el numero menor es:', menor)
cantidad1 = int(input('ingrese la cantidad de numeros que desea: '))
suma = 0
for i in range(cantidad1):
    numero = int(input('ingrese un numero: '))
    suma += numero
print('la suma de los numeros es:', suma)