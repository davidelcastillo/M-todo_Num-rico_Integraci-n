import numpy as np
import matplotlib.pyplot as plt

# Definir los tiempos en minutos desde el inicio (07:30)
tiempos = np.array([0, 15, 30, 45, 75, 105])

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = np.array([18, 24, 14, 24, 21, 9])

# Intervalo de integración
a = tiempos[0]
b = tiempos[-1]
tramos = len(tiempos) - 1

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b - a) / tramos
suma = tasas[0]

for i in range(1, tramos):
    suma += 2 * tasas[i]

suma += tasas[-1]
area = (h * suma) / 2

# Multiplicar el resultado por 4 ya que la tasa es cada 4 minutos
total_vehiculos = area * 4

# SALIDA
print('Tramos: ', tramos)
print('Total de vehículos: ', total_vehiculos)

# GRAFICA
# Puntos de muestra
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
