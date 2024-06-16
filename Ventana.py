import tkinter as tk
import threading
from Ingreso_fechas import*

def mostrar_ventana(Area_trapecio_manual_a, Area_trapecio_compuesto_a, Error_trapecio_compuesto_a, 
                    Area_trapecio_manual_b, Area_trapecio_compuesto_b, Error_trapecio_compuesto_b, 
                    tiempo_a, tiempo_b, a_inc, a_fin, b_inc, b_fin):
    # Función que crea la ventana y la ejecuta en un hilo separado
    def crear_ventana():
        # Crear la ventana principal
        root = tk.Tk()
        root.title("Estimaciones")
        root.configure(bg='#f0f0f0')  # Fondo de la ventana

        # Crear el texto de la primera sección
        text_a = (
            f"ESTIMACIONES\n"
            f"Desde {a_inc} a {a_fin} :\n"
            f"Tramos: {len(tiempo_a) - 1}\n"
            f"Cantidad de autos (Trapecio manual): {Area_trapecio_manual_a}\n"
            f"Cantidad de autos (Trapecio Compuesto): {Area_trapecio_compuesto_a}\n"
            f"Estimación del error (Trapecio Compuesto): {Error_trapecio_compuesto_a}\n"
            f"Diferencia Trapecio manual y Trapecio Compuesto: {abs(Area_trapecio_manual_a - Area_trapecio_compuesto_a)}\n"
        )

        # Crear el texto de la segunda sección
        text_b = (
            f"Desde {b_inc} a {b_fin} :\n"
            f"Tramos: {len(tiempo_b) - 1}\n"
            f"Cantidad de autos (Trapecio manual): {Area_trapecio_manual_b}\n"
            f"Cantidad de autos (Trapecio Compuesto): {Area_trapecio_compuesto_b}\n"
            f"Estimación del error (Trapecio Compuesto): {Error_trapecio_compuesto_b}\n"
            f"Diferencia Trapecio manual y Trapecio Compuesto: {abs(Area_trapecio_manual_b - Area_trapecio_compuesto_b)}\n"
        )

        # Crear un widget de texto
        text_widget = tk.Text(root, wrap="word", bg='#f0f0f0', font=('Helvetica', 12), borderwidth=0)
        text_widget.insert("1.0", text_a + "\n" + text_b)
        text_widget.config(state="disabled", fg='#333333')  # Hacer que el texto sea solo de lectura y cambiar el color del texto
        text_widget.pack(padx=10, pady=10)

        # Ejecutar el bucle principal de la ventana
        root.mainloop()

    # Crear y comenzar un hilo para la ventana de tkinter
    hilo_ventana = threading.Thread(target=crear_ventana)
    hilo_ventana.start()

# Ejemplo de uso
if __name__ == "__main__":
    Area_trapecio_manual_a = 100
    Area_trapecio_compuesto_a = 105
    Error_trapecio_compuesto_a = 0.05
    Area_trapecio_manual_b = 200
    Area_trapecio_compuesto_b = 195
    Error_trapecio_compuesto_b = 0.025
    tiempo_a = [1, 2, 3, 4, 5]
    tiempo_b = [1, 2, 3, 4]

    mostrar_ventana(Area_trapecio_manual_a, Area_trapecio_compuesto_a, Error_trapecio_compuesto_a, 
                    Area_trapecio_manual_b, Area_trapecio_compuesto_b, Error_trapecio_compuesto_b, 
                    tiempo_a, tiempo_b)

    # Aquí puedes continuar con el resto del programa sin que la ventana detenga la ejecución
    print("La ventana se está ejecutando en un hilo separado.")

