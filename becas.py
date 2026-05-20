promedio= float(input("Ingrese su promedio: "))
ingresos= float(input("Ingrese sus ingresos mensuales: "))
if promedio >= 9.5 and ingresos < 50000:
    print("felicidades has obtenido la beca del 100%.")
elif promedio >= 7.5 and ingresos < 75000:
    print("Has obtenido la beca del 50%.")
elif promedio >= 6.5 and ingresos < 100000:
    print("Has obtenido la beca del 25%.")
else:
    print("Lo siento, no has obtenido ninguna beca.")