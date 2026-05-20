contraseña_correcta = "47322523"
intentos = 0

while intentos < 3:
    contraseña = input("Ingrese la contraseña: ")

    if contraseña == contraseña_correcta:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta")

if intentos == 3:
    print("Acceso denegado")