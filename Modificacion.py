import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.integrate import trapezoid
from Ingreso_fechas import *
from Ventana import *


###                          METODOS NUMERICOS
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

def integrate_trapezoid_composite(xi, fi):
    ''' Integral con método del trapecio compuesto '''
    n = len(xi)
    h = xi[1] - xi[0]
    integral = (fi[0] + fi[-1]) / 2 + sum(fi[1:-1])
    integral *= h
    return integral

def trapezoid_error_estimation(xi, fi):
    ''' Estimación del error del método del trapecio compuesto '''
    n = len(xi)
    h = xi[1] - xi[0]
    second_derivatives = np.gradient(np.gradient(fi, h), h)
    max_second_derivative = np.max(np.abs(second_derivatives))
    error_estimate = -((xi[-1] - xi[0]) * h**2 / 12) * max_second_derivative
    return error_estimate

########################################################################
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

# Ingreso de intervalos deseados 
def sub_intervalo (xi, fi,ti):
    while True:
        a_t = input ("Ingrese la hora en formato HH:MM para el inicio del intervalo: ") 
        a_valido = validate_time(a_t)        
        b_t = input ("Ingrese la hora en formato HH:MM para el fin del intervalo: ")        
        b_valido = validate_time(b_t)
        
        try:
            a =  ti.index(a_valido)
            b =  ti.index(b_valido)
            break
        except ValueError:
            print ("Ingresó una hora que no esta en la lista inicial, intente nuevamente: ") 
    
                                                     
    intervalo1 = xi[a:b+1]
    intervalo2 = fi[a:b+1]

    return intervalo1, intervalo2, a_valido, b_valido


# def sub_intervalo(xi, fi, ti):
#     def procesar_entrada():
#         a_t = entry_a.get()
#         b_t = entry_b.get()

#         try:
#             a_valido = validate_time(a_t)
#             b_valido = validate_time(b_t)

#             a = ti.index(a_valido)
#             b = ti.index(b_valido)

#             intervalo1 = xi[a:b+1]
#             intervalo2 = fi[a:b+1]

#             result_var.set((intervalo1, intervalo2, a_valido.strftime('%H:%M'), b_valido.strftime('%H:%M')))
#             root.quit()  # Cerrar la ventana después de procesar correctamente la entrada

#         except ValueError as e:
#             messagebox.showerror("Error", str(e))
#         except Exception as e:
#             messagebox.showerror("Error", f"Error inesperado: {e}")

#     # Crear la ventana principal
#     root = tk.Tk()
#     root.title("Entrada de Intervalos")

#     # Crear una variable de control para almacenar los resultados
#     result_var = tk.Variable(value=None)

#     # Crear etiquetas y campos de entrada
#     label_a = tk.Label(root, text="Ingrese la hora en formato HH:MM para el inicio del intervalo:")
#     label_a.pack(padx=10, pady=5)

#     entry_a = tk.Entry(root, width=25)
#     entry_a.pack(padx=10, pady=5)

#     label_b = tk.Label(root, text="Ingrese la hora en formato HH:MM para el fin del intervalo:")
#     label_b.pack(padx=10, pady=5)

#     entry_b = tk.Entry(root, width=25)
#     entry_b.pack(padx=10, pady=5)

#     # Crear un botón para procesar la entrada
#     boton = tk.Button(root, text="Enviar", command=procesar_entrada)
#     boton.pack(padx=10, pady=10)

#     # Ejecutar el bucle principal de la ventana
#     root.mainloop()

#     # Obtener el resultado almacenado en result_var
#     return result_var.get()

# Inicializar listas para tiempos y tasas
tiempos = []
tasas = []
times = []

# # Solicitar la cantidad de muestras
cantidad = input("Ingrese la cantidad de muestras: ")
cantidad = int(prueba_num(cantidad))



# # Solicitar los tiempos y las tasas para cada muestra
for i in range(cantidad):
     #Ingreso / validacion hora
     time_input = input(f"Ingrese la hora en formato HH:MM de la muestra {i + 1}: ")
     # hora_valida = validate_time(time_input)
     times.append(validate_time(time_input))
    #Ingreso / validacion numero (tasa)
     temptasa = input(f"Ingrese la tasa de la muestra {i + 1}: ")
     tasas.append(float(prueba_num(temptasa)))

tiempos = calculate_time_differences(times)



# # Solicitar el tiempo de duración de las muestras
tiempo_muestra = input("Ingrese el tiempo de duración de las muestras: ")
tiempo_muestra = float(prueba_num(tiempo_muestra))

# Convertir listas a arrays de numpy para realizar operaciones vectorizadas
tiempos = np.array(tiempos)
tasas = np.array(tasas) / tiempo_muestra


# # Definir los tiempos en minutos desde el inicio (07:30)
# tiempos = np.array([0, 15, 30, 45, 75, 105])

# # # Definir las tasas vehiculares (vehículos cada 4 min)
# tasas = np.array([18, 24, 14, 24, 21, 9])
# tasas = tasas/4 #sacar vehiculos por minuto 


print ('Para a :')
# rdo_a = sub_intervalo(tiempos, tasas, times)
# if rdo_a:
#         tiempo_a, tasas_a, a_inc, a_fin = rdo_a
tiempo_a, tasas_a, a_inc, a_fin = sub_intervalo(tiempos, tasas, times)
#Tomar solo hora y min del datetime
a_inc =  a_inc.strftime("%H:%M")
a_fin =  a_fin.strftime("%H:%M")

# PROCEDIMIENTO: Calcular el área usando el método del trapecio en a
Area_trapecio_manual_a = integratrapecio_fi(tiempo_a, tasas_a)
Area_trapecio_compuesto_a = integrate_trapezoid_composite(tiempo_a, tasas_a)
Error_trapecio_compuesto_a = trapezoid_error_estimation(tiempo_a, tasas_a)

print ('Para b :')
# rdo_b = sub_intervalo(tiempos, tasas, times)
# if rdo_b:
#         tiempo_b, tasas_b, b_inc, b_fin = rdo_b
tiempo_b, tasas_b, b_inc, b_fin = sub_intervalo(tiempos, tasas, times)
#Tomar solo hora y min del datetime 
b_inc =  b_inc.strftime("%H:%M")
b_fin =  b_fin.strftime("%H:%M")

# PROCEDIMIENTO: Calcular el área usando el método del trapecio en b
Area_trapecio_manual_b = integratrapecio_fi(tiempo_b, tasas_b)
Area_trapecio_compuesto_b = integrate_trapezoid_composite(tiempo_b, tasas_b)
Error_trapecio_compuesto_b = trapezoid_error_estimation(tiempo_b, tasas_b)

# SALIDA: Mostrar el número de tramos y la cantidad de autos para 
# print ('ESTIMACIONES')
# print ('Desde 07:30 a 09:15 : ')       ## Posible modificacion de esta linea para hacerlo más general 
# print('Tramos: ', len(tiempo_a) - 1)
# print(f"Cantidad de autos (Trapecio manual):  {Area_trapecio_manual_a}")
# print('Cantidad de autos (Trapecio Compuesto): ', Area_trapecio_compuesto_a)
# print('Estimación del error (Trapecio Compuesto): ', Error_trapecio_compuesto_a)
# print('Diferencia Trapecio manual y Trapecio Compuesto: ', abs(Area_trapecio_manual_a - Area_trapecio_compuesto_a))
# print ('Desde 07:30 a 08:15 : ')      ## Posible modificacion de esta linea para hacerlo más general 
# print('Tramos: ', len(tiempo_b) - 1)
# print('Cantidad de autos (Trapecio manual): ', Area_trapecio_manual_b)
# print('Cantidad de autos (Trapecio Compuesto): ', Area_trapecio_compuesto_b)
# print('Estimación del error (Trapecio Compuesto): ', Error_trapecio_compuesto_b)
# print('Diferencia Trapecio manual y Trapecio Compuesto: ', abs(Area_trapecio_manual_b - Area_trapecio_compuesto_b))


mostrar_ventana(Area_trapecio_manual_a, Area_trapecio_compuesto_a, Error_trapecio_compuesto_a, 
                    Area_trapecio_manual_b, Area_trapecio_compuesto_b, Error_trapecio_compuesto_b, 
                    tiempo_a, tiempo_b, a_inc, a_fin, b_inc, b_fin)


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



