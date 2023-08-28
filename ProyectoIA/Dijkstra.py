import heapq
import time

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
RESET_COLOR = '\033[0m'

def dijkstra_laberinto(laberinto, inicio, meta):
    n = len(laberinto)
    m = len(laberinto[0])

    distancias = [[float('inf')] * m for _ in range(n)]
    distancias[inicio[0]][inicio[1]] = 0
    visitados = [[False] * m for _ in range(n)]

    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        x, y = nodo_actual

        if nodo_actual == meta:
            break

        if visitados[x][y]:
            continue

        visitados[x][y] = True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visitados[nx][ny]:
                peso = 1 if laberinto[nx][ny] == 0 else float('inf')
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[nx][ny]:
                    distancias[nx][ny] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, (nx, ny)))

    ruta_minima = reconstruir_ruta(distancias, inicio, meta)
    return ruta_minima


def reconstruir_ruta(distancias, inicio, meta):
    ruta = []
    x, y = meta

    while (x, y) != inicio:
        ruta.append((x, y))
        vecinos = []

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(distancias) and 0 <= ny < len(distancias[0]):
                vecinos.append(((nx, ny), distancias[nx][ny]))

        vecinos.sort(key=lambda v: v[1])

        x, y = vecinos[0][0]
    
    ruta.append(inicio)
    ruta.reverse()
    return ruta

def imprimir_laberinto_con_ruta(laberinto, ruta):
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if (i, j) in ruta:
                color_index = ruta.index((i, j)) % len(COLORS)
                print(COLORS[color_index] + str(celda) + RESET_COLOR, end=' ')
            else:
                print(str(celda), end=' ')
        print()

# Crear el laberinto (cambiarlo por tu laberinto real)
laberinto_ejemplo = [
    [0, 1, 0, 0, 0],
    [2, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 3]
]

inicio_ejemplo = (1, 0)
meta_ejemplo = (4, 4)

inicio_tiempo = time.time()
ruta_minima = dijkstra_laberinto(
    laberinto_ejemplo, inicio_ejemplo, meta_ejemplo)
tiempo_total = time.time() - inicio_tiempo

ruta_minima_str = ' -> '.join(f'({x},{y})' for x, y in ruta_minima)

print("Ruta mínima:", ruta_minima_str)
print("Tiempo total:", tiempo_total, "segundos")

print("Laberinto con Ruta:")
imprimir_laberinto_con_ruta(laberinto_ejemplo, ruta_minima)
