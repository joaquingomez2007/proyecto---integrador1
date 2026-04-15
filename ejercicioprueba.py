gasto_comida = 100000
gasto_sin_alcohol = 50000
gasto_alcohol = 40000

total_invitados = 50
invitados_con_alcohol = 20

# costos base
costo_comida = gasto_comida / total_invitados
costo_sin_alcohol = gasto_sin_alcohol / total_invitados
costo_base = costo_comida + costo_sin_alcohol

# costo alcohol
costo_alcohol = gasto_alcohol / invitados_con_alcohol

print("Cada invitado paga (sin alcohol):", costo_base)
print("Cada invitado que toma alcohol paga:", costo_base + costo_alcohol)