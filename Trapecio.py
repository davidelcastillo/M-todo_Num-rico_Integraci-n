import numpy as np
import matplotlib.pyplot as plt

# Solicitar al usuario la cantidad de datos a ingresar
tiempos = np.array([0, 15, 30, 45, 75, 105])

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = np.array([18, 24, 14, 24, 21, 9])
tasas = tasas/4 #sacar vehiculos por minuto 

    # Convertir las listas a arrays de numpy
tiempos = np.array(tiempos)
tasas = np.array(tasas)

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
total_vehiculos = area 

    # Cálculo de la segunda derivada aproximada
    # f''(x) ≈ (f(x+h) - 2f(x) + f(x-h)) / h^2
segunda_derivada = []
for i in range(1, len(tasas) - 1):
    fxx = (tasas[i + 1] - 2 * tasas[i] + tasas[i - 1]) / (h**2)
    segunda_derivada.append(fxx)

max_segunda_derivada = max(segunda_derivada, key=abs)  # Valor máximo absoluto de la segunda derivada

    # Estimación del error del método del trapecio compuesto
error_trapecio = -((b - a) ** 3 / (12 * tramos ** 2)) * max_segunda_derivada  # Ajuste por la tasa vehicular cada 4 minutos

    # SALIDA
print('Tramos: ', tramos)
print('Total de vehículos: ', total_vehiculos)
print('Error estimado del método del trapecio: ', abs(error_trapecio))

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
