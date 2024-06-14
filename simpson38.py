# Integración Simpson 1/3
# Usando una muestras xi,fi
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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




# Definir los tiempos en minutos desde el inicio (07:30)
tiempos = np.array([0, 15, 30, 45, 75, 105])

# Definir las tasas vehiculares (vehículos cada 4 min)
tasas = np.array([18, 24, 14, 24, 21, 9]) / 4  # Sacar vehículos por minuto

# Interpolar los datos para obtener más puntos
interp_func = interp1d(tiempos, tasas, kind='cubic')
tiempos_interp = np.linspace(tiempos[0], tiempos[-1], 100)  # Generar más puntos para la interpolación
tasas_interp = interp_func(tiempos_interp)

# Ahora puedes usar tiempos_interp y tasas_interp para aplicar el método de Simpson 3/8
resultado = integrasimpson38_fi(tiempos_interp, tasas_interp)
print('Resultado de la integral (Simpson 3/8):', resultado)