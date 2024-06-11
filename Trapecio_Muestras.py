import numpy as np
import matplotlib.pyplot as plt

def integratrapecio_fi(xi, fi):
    '''Sobre muestras de fi para cada xi
       integral con método de trapecio
    '''
    n = len(xi)
    suma = 0
    for i in range(n - 1):
        dx = xi[i + 1] - xi[i]
        untrapecio = dx * (fi[i + 1] + fi[i]) / 2
        suma += untrapecio
    return suma

# INGRESO DE DATOS POR CONSOLA
num_datos = int(input("Ingrese la cantidad de datos: "))
tiempo_duracion = int(input("Ingrese la duracion en min del intervalo: "))

tiempos = []
tasas = []

for i in range(num_datos):
    tiempo = float(input(f"Ingrese el tiempo en minutos para el dato {i + 1}: "))
    tasa = float(input(f"Ingrese la tasa de vehículos (vehículos cada 4 minutos) para el dato {i + 1}: "))
    tiempos.append(tiempo)
    tasas.append(tasa)

# Convertir las listas a arrays de numpy
tiempos = np.array(tiempos)
tasas = np.array(tasas)

# PROCEDIMIENTO
Area = integratrapecio_fi(tiempos, tasas)

# Multiplicar el resultado por 4 ya que la tasa es cada 4 minutos
total_vehiculos = Area * tiempo_duracion

# SALIDA
print('Tramos: ', len(tiempos) - 1)
print('Total de vehículos: ', total_vehiculos)

# GRAFICA
# Puntos de muestra
xi = tiempos
fi = tasas
# Linea suave
muestraslinea = len(tiempos) * 10
xk = np.linspace(tiempos[0], tiempos[-1], muestraslinea)
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
for i in range(len(xi)):
    plt.axvline(xi[i], color='w')

plt.grid(True)
plt.show()
