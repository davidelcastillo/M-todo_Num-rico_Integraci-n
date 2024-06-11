from Trapecio import *

# Solicitar al usuario la cantidad de datos a ingresar
num_datos = int(input("Ingrese la cantidad de datos: "))
tiempo_duracion = int(input("Ingrese la duracion en min del intervalo: "))

tiempos = []
tasas = []

# Solicitar al usuario los tiempos y las tasas vehiculares
# for i in range(num_datos):
#      tiempo = float(input(f"Ingrese el tiempo en minutos para el dato {i + 1}: "))
#      tasa = float(input(f"Ingrese la tasa de vehículos (vehículos cada 4 minutos) para el dato {i + 1}: "))
#      tiempos.append(tiempo)
#      tasas.append(tasa)

# Definir los tiempos en minutos desde el inicio (07:30)
tiempos = [0, 15, 30, 45, 75, 105]

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = [18, 24, 14, 24, 21, 9]

trapecio (tiempos,tasas, num_datos, tiempo_duracion)