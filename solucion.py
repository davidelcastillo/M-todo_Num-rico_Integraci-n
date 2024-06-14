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

def integrasimpson38_fi(xi,fi,tolera = 1e-10):
    ''' sobre muestras de fi para cada xi
        integral con método de Simpson 3/8
        respuesta es np.nan para tramos desiguales,
        no hay suficientes puntos.
    '''
    n = len(xi)
    i = 0
    suma = 0
    while not(i>=(n-3)):
        h  = xi[i+1]-xi[i]
        h1 = (xi[i+2]-xi[i+1])
        h2 = (xi[i+3]-xi[i+2])
        dh = abs(h-h1)+abs(h-h2)
        if dh<tolera:# tramos iguales
            unS38 = fi[i]+3*fi[i+1]+3*fi[i+2]+fi[i+3]
            unS38 = (3/8)*h*unS38
            suma = suma + unS38
        else:  # tramos desiguales
            suma = 'tramos desiguales'
        i = i + 3
    if (i+1)<n: # incompleto, tramos por calcular
        suma = 'tramos incompletos, faltan '
        suma = suma +str(n-(i+1))+' tramos'
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

# PROCEDIMIENTO
Area = integrasimpson38_fi(tiempos,tasas)

# SALIDA
print('tramos: ',len(tiempos)-1)
print('Integral con Simpson 1/3: ',Area)
if type(Area)==str:
    print('  Revisar errores...')

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
