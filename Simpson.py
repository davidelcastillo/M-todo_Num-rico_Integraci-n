import numpy as np

def simpson_compuesto(tiempos, tasas):
    n = len(tiempos)
    h = (tiempos[-1] - tiempos[0]) / (n - 1)
    suma = tasas[0] + tasas[-1]

    for i in range(1, n - 1):
        if i % 2 == 0:
            suma += 2 * tasas[i]
        else:
            suma += 4 * tasas[i]

    return (h * suma) / 3

# Ejemplo de uso
tiempos = np.array([0, 15, 30, 45, 75, 105])
tasas = np.array([18, 24, 14, 24, 21, 9])

total_vehiculos_simpson = simpson_compuesto(tiempos, tasas) 
print('Total de vehículos usando Simpson compuesto:', total_vehiculos_simpson)
