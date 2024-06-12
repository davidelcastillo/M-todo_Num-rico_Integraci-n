# Integración: Regla de los trapecios
# Usando una muestras xi,fi
#aplica el metodo trapecio dato por dato asi ajustar h
import numpy as np
import matplotlib.pyplot as plt

def integratrapecio_fi(xi,fi):
    ''' sobre muestras de fi para cada xi
        integral con método de trapecio
    '''
    n = len(xi)
    suma = 0
    for i in range(0,n-1,1):
        dx = xi[i+1]-xi[i]
        untrapecio = dx*(fi[i+1]+fi[i])/2
        suma = suma + untrapecio
    return(suma)

# PROGRAMA -----------------
# INGRESO
# Definir los tiempos en minutos desde el inicio (07:30)
tiempos = np.array([0, 15, 30, 45, 75, 105])

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = np.array([18, 24, 14, 24, 21, 9])
tasas = tasas/4 #sacar vehiculos por minuto 

# PROCEDIMIENTO
Area = integratrapecio_fi(tiempos,tasas)

# SALIDA
print('tramos: ',len(tiempos)-1)
print('Cantidad de autos: ',Area)


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
