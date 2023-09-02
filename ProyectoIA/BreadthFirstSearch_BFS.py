# Algoritmo de busqueda en anchura o Breadth-First Search (BFS) para encontrar la ruta más corta en un laberinto
# Recibe la matriz, las coordenadas de inicio y las coordenadas de la meta
# la matriz contiene elementos del 0 a 3, donde 0 es un espacio vacio, 1 es un obstaculo,
# 2 es el punto de inicio y 3 es el punto de meta
# no se puede pasar por los obstaculos, solo por los espacios vacios
# Se debe retornar la ruta mas corta desde el punto de inicio hasta el punto de meta en un string

import time
import memory_profiler
from collections import deque
import numpy as np  # Agregar numpy para matrices más eficientes

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m',
          '\033[33m', '\033[96m', '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
RESET_COLOR = '\033[0m'


class BFS:
    # Movimientos en x, arriba y abajo, no se puede mover en diagonal
    dx = [-1, 1, 0, 0]
    # Movimientos en y, izquierda y derecha, no se puede mover en diagonal
    dy = [0, 0, -1, 1]

    def __init__(self, laberinto, inicio, meta):
        # Usar una matriz numpy para acceso más rápido
        self.laberinto = np.array(laberinto)
        self.inicio = inicio
        self.meta = meta
        self.n, self.m = self.laberinto.shape
        self.ruta_minima = []
        self.queue = deque([(self.inicio, [])])
        # Usar matriz numpy de booleanos
        self.visitado = np.zeros_like(self.laberinto, dtype=bool)
        # Asegurarse de que la celda de meta no esté marcada como visitada
        self.visitado[self.meta[0], self.meta[1]] = False

    def bfs_laberinto(self):
        while self.queue:  # Mientras la cola no esté vacía
            # Obtener el primer elemento de la cola
            (x, y), ruta_minima = self.queue.popleft()

            if (x, y) == self.meta:  # Si la celda actual es la meta, retornar la ruta actual
                # Agregar la coordenada de inicio al principio de la ruta
                ruta_minima.insert(0, self.inicio)
                return ruta_minima

            for i in range(4):
                # Obtener las nuevas coordenadas de la celda a la que se puede mover
                new_x = x + self.dx[i]
                # Obtener las nuevas coordenadas de la celda a la que se puede mover
                new_y = y + self.dy[i]

                if (
                    0 <= new_x < self.n
                    and 0 <= new_y < self.m  # Si las nuevas coordenadas están dentro de los límites
                    # Para considerar la meta con valor 3, y no considerar los obstáculos con valor 1
                    and self.laberinto[new_x][new_y] != 1
                    # Si la celda no ha sido visitada
                    and not self.visitado[new_x][new_y]
                ):
                    # Marcar la celda como visitada
                    self.visitado[new_x][new_y] = True
                    # Agregar la celda a la ruta actual
                    nueva_ruta = ruta_minima + [(new_x, new_y)]
                    # Agregar la celda a la cola con la ruta actual
                    self.queue.append(((new_x, new_y), nueva_ruta))

        return None  # Si no se encontró una ruta, retornar None

    def imprimir_laberinto_con_ruta(self, ruta):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in ruta:
                    color_index = ruta.index((i, j)) % len(COLORS)
                    print(COLORS[color_index] +
                          str(self.laberinto[i, j]) + RESET_COLOR, end=' ')
                else:
                    print(self.laberinto[i, j], end=' ')
            print()

    def resolver_laberinto(self):
        print("Resolviendo laberinto con BFS...")
        inicio_tiempo = time.time()
        mem_usage = memory_profiler.memory_usage()
        ruta_minima = self.bfs_laberinto()

        # Obtener el consumo de memoria y tiempo de ejecución
        mem_usage_end = memory_profiler.memory_usage()
        tiempo_total = time.time() - inicio_tiempo

        print("\nTiempo de ejecución:", tiempo_total, "segundos")
        print("Consumo de memoria:", max(mem_usage_end) - max(mem_usage), "MB")

        if ruta_minima is not None:
            ruta_minima_str = ' -> '.join(f'({x},{y})' for x, y in ruta_minima)
            print("Ruta mínima:", ruta_minima_str)
            print("\nLaberinto con Ruta:")
            self.imprimir_laberinto_con_ruta(ruta_minima)
        else:
            ruta_minima_str = "No se encontró una ruta."
            print("Ruta mínima:", ruta_minima_str)


if __name__ == '__main__':
    # Definir la matriz de ejemplo y coordenadas de inicio y meta
    laberinto_ejemplo = [
        [2, 0, 3],
        [1, 1, 0],
        [0, 0, 0]
    ]

    inicio = None
    meta = None

    for i in range(len(laberinto_ejemplo)):
        for j in range(len(laberinto_ejemplo[0])):
            if laberinto_ejemplo[i][j] == 2:
                inicio = (i, j)
            elif laberinto_ejemplo[i][j] == 3:
                meta = (i, j)

    bfs_solver = BFS(laberinto_ejemplo, inicio, meta)
    bfs_solver.resolver_laberinto()
