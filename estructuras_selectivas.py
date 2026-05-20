n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 < n2:
    n1, n2 = n2, n1

if n1 < n3:
    n1, n3 = n3, n1

if n2 < n3:
    n2, n3 = n3, n2

print(n1, n2, n3)

peso = float(input("Ingrese el peso del paquete (kg): "))
destino = input("Ingrese el destino (capital/interior): ").lower()
cliente = input("Ingrese el tipo de cliente (normal/premium): ").lower()

if peso <= 5:
    costo = 2000
elif peso <= 20:
    costo = 5000
else:
    costo = 10000

if destino == "interior":
    costo = costo * 1.15  # +15%

if cliente == "premium":
    costo = costo * 0.80  # -20%

print("Costo final:", costo)