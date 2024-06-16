from datetime import datetime

def input_times(n):
    times = []
    for _ in range(n):
        time_input = input("Ingrese la hora en formato HH:MM: ")
        times.append(datetime.strptime(time_input, "%H:%M"))
    return times

def validate_time (hora) :
     while True:
        try:
            time_obj = datetime.strptime(hora, "%H:%M")
            return time_obj
        except ValueError:
            print("Error: ingrese una hora válida en formato HH:MM.")
            hora = input("Ingrese nuevamente la hora en formato HH:MM: ")

def calculate_time_differences(times):
    differences = []
    for i, time in enumerate(times):
        if i == 0:
            differences.append(0)
        else:
            diff = (time - times[0]).seconds // 60
            differences.append(diff)
    return differences

def main():
    n = int(input("Ingrese la cantidad de datos horarios: "))
    times = input_times(n)
    differences = calculate_time_differences(times)
    print("Las diferencias en minutos son:", differences)

if __name__ == "__main__":
    main()