meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

unidades = [10, 8, 9, 10, 10, 20, 5, 9, 8, 7, 5, 10]

costos = [10, 12, 11, 12, 10, 9, 14, 10, 11, 12, 15, 11]


suma_unidades = 0
total_costos = 0


menor = costos[0]
pos_menor = 0


for i in range(12):

    
    suma_unidades = suma_unidades + unidades[i]

    
    total_costos = total_costos + (unidades[i] * costos[i])

  
    if costos[i] < menor:
        menor = costos[i]
        pos_menor = i


promedio_unidades = suma_unidades / 12
promedio_costos = total_costos / 12


print("Promedio de unidades:", promedio_unidades)
print("Promedio del costo anual:", promedio_costos)
print("Mes con menor costo:", meses[pos_menor])