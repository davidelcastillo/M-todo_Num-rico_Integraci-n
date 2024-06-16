import numpy as np
import matplotlib.pyplot as plt

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

# Solicitar los tiempos y las tasas para cada muestra
for i in range(cantidad):
    temptiempo = input(f"Ingrese el tiempo de la muestra {i + 1}: ")
    tiempos.append(float(prueba_num(temptiempo)))
    temptasa = input(f"Ingrese la tasa de la muestra {i + 1}: ")
    tasas.append(float(prueba_num(temptasa)))

# Solicitar el tiempo de duración de las muestras
tiempo_muestra = input("Ingrese el tiempo de duración de las muestras: ")
tiempo_muestra = float(prueba_num(tiempo_muestra))

# Convertir listas a arrays de numpy para realizar operaciones vectorizadas
tiempos = np.array(tiempos)
tasas = np.array(tasas) / tiempo_muestra

# PROCEDIMIENTO: Calcular el área usando el método del trapecio
Area = integratrapecio_fi(tiempos, tasas)

# SALIDA: Mostrar el número de tramos y la cantidad de autos
print('Tramos: ', len(tiempos) - 1)
print('Cantidad de autos: ', Area)


# GRAFICA
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



