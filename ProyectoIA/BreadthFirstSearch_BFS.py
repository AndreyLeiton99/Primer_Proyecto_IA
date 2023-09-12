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
from MetodosDeImpresion import imprimir_datos


class BFS:
    # Movimientos en x, arriba y abajo, y en y, izquierda y derecha, y diagonales
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

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
            # Obtener el primer elemento de la cola, para obtener la celda actual y la ruta actual
            (x, y), ruta_minima = self.queue.popleft()

            if (x, y) == self.meta:  # Si la celda actual es la meta, retornar la ruta actual, que ya contiene los elementos de la ruta mínima
                # Agregar la coordenada de inicio al principio de la ruta
                ruta_minima.insert(0, self.inicio)
                return ruta_minima

            for i in range(8):  # Ahora se consideran las 8 direcciones posibles (incluyendo diagonales)
                # Obtener las nuevas coordenadas de la celda a la que se puede mover
                new_x = x + self.dx[i]
                new_y = y + self.dy[i]

                self.actualizar_ruta_minima(ruta_minima, new_x, new_y)  # Actualizar la ruta mínima, para cada vecino
        return None

    def actualizar_ruta_minima(self, ruta_minima, new_x, new_y): # Verificar que las nuevas coordenadas estén dentro de los límites
        if (
                    0 <= new_x < self.n
                    and 0 <= new_y < self.m  # Si las nuevas coordenadas están dentro de los límites
                    # Si la celda no es un obstáculo
                    and self.laberinto[new_x][new_y] != 1
                    # Si la celda no ha sido visitada antes
                    and not self.visitado[new_x][new_y]
                ):
                    # Marcar la celda como visitada
            self.visitado[new_x][new_y] = True
                    # Agregar la celda a la ruta actual, que es la ruta mínima hasta el momento
            nueva_ruta = ruta_minima + [(new_x, new_y)]
                    # Agregar la celda a la cola con la ruta actual, para seguir buscando desde esa celda en la siguiente iteración
            self.queue.append(((new_x, new_y), nueva_ruta)) 

    def resolver_laberinto(self, algoritmo, nombre_laberinto):
        print("Resolviendo laberinto con BFS...")
        inicio_tiempo = time.time()
        mem_usage = memory_profiler.memory_usage()
        ruta_minima = self.bfs_laberinto()

        # Obtener el consumo de memoria y tiempo de ejecución
        mem_usage_end = memory_profiler.memory_usage()
        tiempo_total = time.time() - inicio_tiempo

        imprimir_datos(mem_usage, ruta_minima, mem_usage_end, tiempo_total, self.laberinto, self.n, self.m, algoritmo, nombre_laberinto)


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

    bfs_solver = BFS(laberinto_ejemplo, inicio, meta)
    bfs_solver.resolver_laberinto("BFS")
