import csv
import glob
import os


def cargar_laberinto(ruta_archivo):
    laberinto = []
    inicio = None
    meta = None

    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo, delimiter=';')
        for fila in lector_csv:
            laberinto.append([int(celda) for celda in fila])

    # Encontrar las coordenadas del punto de inicio y la meta
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 2:
                inicio = (i, j)
            elif laberinto[i][j] == 3:
                meta = (i, j)

    return laberinto, inicio, meta


def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(' '.join(str(celda) for celda in fila))


def obtener_ruta_matriz_mas_actualizada(carpeta):
    archivos_csv = glob.glob(os.path.join(carpeta, 'Matriz_*.csv'))
    consecutivos = []

    for nombre in archivos_csv:
        base_nombre = os.path.basename(nombre)
        partes_nombre = base_nombre.split('_')

        if len(partes_nombre) == 2 and partes_nombre[0] == 'Matriz':
            try:
                consecutivo = int(partes_nombre[1].split('.')[0])
                consecutivos.append(consecutivo)
            except ValueError:
                pass

    if consecutivos:
        consecutivo_maximo = max(consecutivos)
    else:
        consecutivo_maximo = 0

    ruta_archivo = os.path.join(carpeta, f"Matriz_{consecutivo_maximo}.csv")
    print(f"Archivo más actualizado: {ruta_archivo}")
    return ruta_archivo

# Obtener la ruta del directorio donde se encuentra el archivo csv
    """_summary_
directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_matrices = os.path.join(directorio_actual, 'MatricesGeneradas')
ruta_archivo = obtener_ruta_matriz_mas_actualizada(carpeta_matrices)

laberinto, inicio, meta = cargar_laberinto(ruta_archivo)

print("Laberinto:")
imprimir_laberinto(laberinto)

print("\nCoordenadas del punto de inicio:", inicio)
print("Coordenadas del punto final:", meta)
    """
