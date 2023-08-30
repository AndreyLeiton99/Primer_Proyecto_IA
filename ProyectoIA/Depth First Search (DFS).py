# Algritmo de depht first search (DFS) para encontrar el camnino mas corto
# Recibe la matriz, las coordenadas de inicio y las coordenadas de la meta
# la matriz contiene elementos del 0 a 3, donde 0 es un espacio vacio, 1 es un obstaculo, 
# 2 es el punto de inicio y 3 es el punto de meta
# no se puede pasar por los obstaculos, solo por los espacios vacios
# Se debe retornar la ruta mas corta desde el punto de inicio hasta el punto de meta en un string
# ademas el tiempo que se demora en encontrar la ruta mas corta y la cantidad de memoria consumida
# se debe imprimir la matriz final con el recorrido de la ruta minima con un color diferente
# y cambiando por un 4 los espacios que ya se recorrieron y no estan en la ruta mas corta

import heapq
import time
import memory_profiler
import subprocess

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[33m', '\033[96m'
          , '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
RESET_COLOR = '\033[0m'

class DFS:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.n = len(laberinto)
        self.m = len(laberinto[0])
        self.camino_actual = []
        self.ruta_minima = []
        self.visitados = [[False] * self.m for _ in range(self.n)]  # Inicializar la matriz de visitados

    def dfs_laberinto(self, x, y):
       # print("Visitados", self.visitados)
        if x < 0 or x >= self.n or y < 0 or y >= self.m or self.laberinto[x][y] == 1 or self.visitados[x][y]:
            return

        self.visitados[x][y] = True  # Marcar como visitado
        self.camino_actual.append((x, y))

        if (x, y) == self.meta:
            if not self.ruta_minima or len(self.camino_actual) < len(self.ruta_minima):
                self.ruta_minima = self.camino_actual.copy()

        self.dfs_laberinto(x + 1, y)
        self.dfs_laberinto(x - 1, y)
        self.dfs_laberinto(x, y + 1)
        self.dfs_laberinto(x, y - 1)

        self.visitados[x][y] = False  # Marcar como no visitado
        self.camino_actual.pop()

    def encontrar_ruta_minima(self):
        self.dfs_laberinto(self.inicio[0], self.inicio[1])
        print("La ruta mínima corresponde a:", self.ruta_minima)
        return self.ruta_minima


    def reconstruir_ruta(self):
        ruta = []
        x, y = self.meta

        while (x, y) != self.inicio:
            ruta.append((x, y))
            vecinos = []

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.m:
                    vecinos.append(((nx, ny), self.distancias[nx][ny]))

            vecinos.sort(key=lambda v: v[1])

            x, y = vecinos[0][0]

        ruta.append(self.inicio)
        ruta.reverse()
        return ruta

    def imprimir_laberinto_con_ruta(self, ruta):
        for i, fila in enumerate(self.laberinto):
            for j, celda in enumerate(fila):
                if (i, j) in ruta:
                    color_index = ruta.index((i, j)) % len(COLORS)
                    print(COLORS[color_index] + str(celda) + RESET_COLOR, end=' ')
                else:
                    print(str(celda), end=' ')
            print()

    def resolver_laberinto(self):
            inicio_tiempo = time.time()
            mem_usage = memory_profiler.memory_usage()
            ruta_minima = self.encontrar_ruta_minima()
            mem_usage_end = memory_profiler.memory_usage()
            tiempo_total = time.time() - inicio_tiempo
            
            ruta_minima_str = ' -> '.join(f'({x},{y})' for x, y in ruta_minima)

            print("\nTiempo de ejecución:", tiempo_total, "segundos")  
            print("Consumo de memoria:", max(mem_usage_end) - max(mem_usage), "MB")          
            print("Ruta mínima:", ruta_minima_str)
            print("\nLaberinto con Ruta:")
            self.imprimir_laberinto_con_ruta(ruta_minima)



if __name__ == '__main__':
    # Definir la matriz de ejemplo y coordenadas de inicio y meta
    laberinto_ejemplo = [
    [2, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 3]
    ]

    inicio = None
    meta = None

    for i in range(len(laberinto_ejemplo)):
        for j in range(len(laberinto_ejemplo[0])):
            if laberinto_ejemplo[i][j] == 2:
                inicio = (i, j)
            elif laberinto_ejemplo[i][j] == 3:
                meta = (i, j)

 
    DFS = DFS(laberinto_ejemplo, inicio, meta)
    DFS.resolver_laberinto()
    print(DFS.encontrar_ruta_minima())

