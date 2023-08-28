import csv

def cargar_laberinto(nombre_archivo):
    laberinto = []
    inicio = None
    meta = None

    with open(nombre_archivo, 'r') as archivo:
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

# Cambiar el nombre del archivo por el nombre de tu archivo CSV
nombre_archivo = 'Matriz.csv'
laberinto, inicio, meta = cargar_laberinto(nombre_archivo)

print("Laberinto:")
imprimir_laberinto(laberinto)

print("\nCoordenadas del punto de inicio:", inicio)
print("Coordenadas del punto final:", meta)


