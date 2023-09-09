import datetime

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m',
          '\033[33m', '\033[96m', '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
RESET_COLOR = '\033[0m'

def imprimir_datos(mem_usage, ruta_minima, mem_usage_end, tiempo_total, laberinto, n, m, algoritmo):
        print("\nTiempo de ejecución:", round(tiempo_total, 2), "segundos")
        print("Consumo de memoria:", max(mem_usage_end) - max(mem_usage), "MB")

        if ruta_minima:
            ruta_minima_str = ' -> '.join(f'({x},{y})' for x, y in ruta_minima)
            print("Ruta mínima:", ruta_minima_str)
            print("\nLaberinto con Ruta:")
            imprimir_laberinto_con_ruta(ruta_minima, laberinto, n, m)
            guardarInfo(mem_usage, mem_usage_end, tiempo_total, algoritmo)
        else:
            ruta_minima_str = "No se encontró una ruta."
            print("Ruta mínima:", ruta_minima_str)

# Imprimir el laberinto con la ruta mínima resaltada en colores
def imprimir_laberinto_con_ruta(ruta, laberinto, n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            if (i, j) in ruta:
                color_index = ruta.index((i, j)) % len(COLORS)
                fila.append(COLORS[color_index] + str(laberinto[i][j]) + RESET_COLOR)
                print(COLORS[color_index] +
                        str(laberinto[i][j]) + RESET_COLOR, end=' ')
            else:
                fila.append(laberinto[i][j])
                print(laberinto[i][j], end=' ')
        matriz.append(fila)
        print()
    return matriz

def linea(caracter, longitud):
    linea = caracter * longitud
    return linea + str(datetime.datetime.now()) + linea + "\n\n"
    
def guardarInfo(mem_usage, mem_usage_end, tiempo_total, algoritmo):
    # ruta del archivo
    ruta_archivo = 'ProyectoIA/InfoAlgoritmos/resultados.txt'
    # Tiempo de ejecucion y consumo de memoria
    execution_time = "Se ejecuta en: %s segundos" % (round(tiempo_total, 2))
    memory = "Consumo de memoria: %d MB\n\n" % (max(mem_usage_end) - max(mem_usage))
    
    # Obtener la fecha y hora actuales
    fecha_hora_actual = datetime.datetime.now()
    
    # el segundo param "a" es para indicar que agregue al final del archivo
    with open(ruta_archivo, 'a') as archivo: 
        archivo.write(linea("=", 40))
        archivo.write(f"- Algoritmo '{algoritmo}'")
        archivo.write("\n- " + execution_time)
        archivo.write("\n- " + memory)    

    

