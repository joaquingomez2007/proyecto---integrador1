num1 = float(input("Primer número: "))
op = input("Operación (+, -, *, /): ")
num2 = float(input("Segundo número: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op== "/" and num2 == 0:
    print("Error: No se puede dividir por cero") 
else:
    print("Operación no válida")