# Tiempos en minutos
tiempos = [450, 465, 480, 495, 525, 555]
# Tasas vehiculares cada 4 minutos
tasas = [18, 24, 14, 24, 21, 9]

# Calcular el total de vehículos que pasan entre las 07:30 y las 09:15
total_vehiculos = sum(tasas) * ((555 - 450) // 4 + 1)

print("Total de vehículos que circulan entre 07:30 y 09:15:", total_vehiculos)
