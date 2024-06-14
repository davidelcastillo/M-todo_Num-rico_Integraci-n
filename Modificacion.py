import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.integrate import trapezoid
from Ingreso_fechas import *

def integratrapecio_fi(xi, fi):
    ''' sobre muestras de fi para cada xi
        integral con método de trapecio
    '''
    n = len(xi)
    suma = 0
    for i in range(n - 1):
        dx = xi[i + 1] - xi[i]
        untrapecio = dx * (fi[i + 1] + fi[i]) / 2
        suma += untrapecio
    return suma

def integra_simpson(xi, fi):
    ''' sobre muestras de fi para cada xi
        integral con método de Simpson
    '''
    n = len(xi)
    if n % 2 == 0:
        n -= 1  # Simpson requiere un número impar de puntos
    h = (xi[-1] - xi[0]) / (n - 1)
    suma = fi[0] + fi[n-1]
    for i in range(1, n-1, 2):
        suma += 4 * fi[i] + 2 * fi[i+1]
    suma += 4 * fi[n-2]
    return h / 3 * suma

def prueba_num(prueba):
    ban = True
    while ban:
        try:
            prueba = float(prueba)
            if prueba < 0:
                print("Error: ingrese un valor válido")
                prueba = input("Ingrese nuevamente: ")
            else:
                ban = False
        except ValueError:
            print("Error: ingrese un número válido")
            prueba = input("Ingrese nuevamente: ")
    return prueba

# Solicitar la cantidad de muestras
cantidad = input("Ingrese la cantidad de muestras: ")
cantidad = int(prueba_num(cantidad))

# Inicializar listas para tiempos y tasas
tiempos = []
tasas = []
times = []

# Solicitar los tiempos y las tasas para cada muestra
# for i in range(cantidad):
#     #Ingreso / validacion hora
#     time_input = input(f"Ingrese la hora en formato HH:MM de la muestra {i + 1}: ")
#     # hora_valida = validate_time(time_input)
#     times.append(validate_time(time_input))
#     #Ingreso / validacion numero (tasa)
#     temptasa = input(f"Ingrese la tasa de la muestra {i + 1}: ")
#     tasas.append(float(prueba_num(temptasa)))

# tiempos = calculate_time_differences(times)



# Solicitar el tiempo de duración de las muestras
# tiempo_muestra = input("Ingrese el tiempo de duración de las muestras: ")
# tiempo_muestra = float(prueba_num(tiempo_muestra))

# # Convertir listas a arrays de numpy para realizar operaciones vectorizadas
# tiempos = np.array(tiempos)
# tasas = np.array(tasas) / tiempo_muestra


# Definir los tiempos en minutos desde el inicio (07:30)
tiempos = np.array([0, 15, 30, 45, 75, 105])

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = np.array([18, 24, 14, 24, 21, 9])
tasas = tasas/4 #sacar vehiculos por minuto 

# PROCEDIMIENTO: Calcular el área usando el método del trapecio
Area_trapecio_manual = integratrapecio_fi(tiempos, tasas)
Area_simpson = integra_simpson(tiempos, tasas)
Area_trapecio_scipy = trapezoid(tasas, tiempos)

# SALIDA: Mostrar el número de tramos y la cantidad de autos
print('Tramos: ', len(tiempos) - 1)
print('Cantidad de autos (Trapecio manual): ', Area_trapecio_manual)
print('Cantidad de autos (Simpson): ', Area_simpson)
print('Cantidad de autos (Trapecio SciPy): ', Area_trapecio_scipy)
print('Diferencia Trapecio manual y Simpson: ', abs(Area_trapecio_manual - Area_simpson))
print('Diferencia Trapecio manual y Trapecio SciPy: ', abs(Area_trapecio_manual - Area_trapecio_scipy))
print('Diferencia Simpson y Trapecio SciPy: ', abs(Area_simpson - Area_trapecio_scipy))


#                                   GRAFICA
# Puntos de muestra
a = tiempos[0]
b = tiempos[-1]
tramos = len(tiempos) - 1
muestras = tramos + 1
xi = tiempos
fi = tasas
# Linea suave
muestraslinea = tramos * 10 + 1
xk = np.linspace(a, b, muestraslinea)
fk = np.interp(xk, xi, fi)  # Interpolar para una línea suave

# Graficando
plt.plot(xk, fk, label='Tasa vehicular (Interpolada)')
plt.plot(xi, fi, marker='o', color='orange', label='Muestras')

plt.xlabel('Tiempo (min)')
plt.ylabel('Vehículos cada 4 min')
plt.title('Integral: Regla de Trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi, 0, fi, color='g', alpha=0.5)
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w')

plt.grid(True)
plt.show()



