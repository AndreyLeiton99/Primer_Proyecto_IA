# Método que realice una matriz aleatoria de n x m, donde n y m son números enteros positivos
# donde la matriz va a estar separada por ; y cada celda va a tener un valor de 0 o 3
# que representan: 
# 0 – Espacios por los cuales puede moverse el agente 
# 1 – Paredes o obstáculos donde no se permite al agente caminar por ahí 
# 2 – El punto de inicio 
# 3 – El punto final o meta
# solo puede haber un inicio y un final, los obstaculos pueden ser los que sean, siempre que haya un camino para llegar al final
# el metodo debe recibir como parametros n y m, que son los numeros de filas y columnas respectivamente
# y debe retornar la matriz aleatoria en un archivo CSV llamado Matriz_consecutivo.csv guardado en la carpeta del proyecto

import os
import csv
import random

def generar_matriz_aleatoria(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("n y m deben ser números enteros positivos")

    matriz = [[0] * m for _ in range(n)]

    inicio = (random.randint(0, n - 1), random.randint(0, m - 1))
    meta = (random.randint(0, n - 1), random.randint(0, m - 1))
    while meta == inicio:
        meta = (random.randint(0, n - 1), random.randint(0, m - 1))

    matriz[inicio[0]][inicio[1]] = 2
    matriz[meta[0]][meta[1]] = 3

    obstaculos = random.randint(1, n * m // 2)
    for _ in range(obstaculos):
        x = random.randint(0, n - 1)
        y = random.randint(0, m - 1)
        while (x, y) == inicio or (x, y) == meta or matriz[x][y] == 1:
            x = random.randint(0, n - 1)
            y = random.randint(0, m - 1)
        matriz[x][y] = 1

    return matriz

def guardar_matriz_en_csv(matriz, archivo):
    with open(archivo, 'w', newline='') as file:
        print(f"Guardando archivo en: {archivo}")
        writer = csv.writer(file, delimiter=';')
        for fila in matriz:
            writer.writerow(fila)

def generar_y_guardar_matriz(n, m):
    # Obtener la ruta del directorio actual donde se encuentra el script
    directorio_actual = os.path.dirname(__file__)
    
    carpeta_destino = os.path.join(directorio_actual, "MatricesGeneradas")
    
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    
    archivo_base = "Matriz"
    
    consecutivo = 1
    archivo_actual = archivo_base
    while os.path.exists(os.path.join(carpeta_destino, f"{archivo_actual}_{consecutivo}.csv")):
        consecutivo += 1
    
    matriz_aleatoria = generar_matriz_aleatoria(n, m)
    archivo_path = os.path.join(carpeta_destino, f"{archivo_actual}_{consecutivo}.csv")
    
    print(f"Matriz aleatoria generada y guardada en {archivo_path}")
    guardar_matriz_en_csv(matriz_aleatoria, archivo_path)
    

if __name__ == "__main__":
    n = 6  # Cambiar según lo deseado
    m = 8  # Cambiar según lo deseado
    generar_y_guardar_matriz(n, m)