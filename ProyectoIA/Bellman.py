# Algoritmo de Bellman para encontrar la ruta mínima en un laberinto
# Recibe la matriz, las coordenadas de inicio y las coordenadas de la meta
# la matriz contiene elementos del 0 a 3, donde 0 es un espacio vacio, 1 es un obstaculo,
# 2 es el punto de inicio y 3 es el punto de meta
# no se puede pasar por los obstaculos, solo por los espacios vacios
# Se debe retornar la ruta mas corta desde el punto de inicio hasta el punto de meta en un string

import time
import memory_profiler
import numpy as np  # Agregar numpy para matrices más eficientes

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m',
          '\033[33m', '\033[96m', '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
RESET_COLOR = '\033[0m'


class Bellman:

    # Movimientos en x, arriba y abajo, no se puede mover en diagonal
    dx = [-1, 1, 0, 0]
    # Movimientos en y, izquierda y derecha, no se puede mover en diagonal
    dy = [0, 0, -1, 1]

    def __init__(self, laberinto, inicio, meta):
        # Convertir la matriz a un arreglo de numpy para mayor eficiencia
        self.laberinto = np.array(laberinto)
        self.inicio = inicio
        self.meta = meta
        self.n, self.m = self.laberinto.shape  # Obtener las dimensiones del laberinto
        # Matriz para guardar las distancias de cada celda en el laberinto
        self.distancias = np.full((self.n, self.m), float('inf'))
        # La distancia de la celda de inicio a si misma es 0
        self.distancias[inicio] = 0
        # Matriz para guardar los padres de cada celda en el laberinto
        self.padres = np.empty((self.n, self.m), dtype=object)
        # Matriz para marcar las celdas visitadas en el laberinto
        self.visitado = np.zeros_like(self.laberinto, dtype=bool)
        # Marcar la celda de meta como visitada para evitar que se agregue a la cola de prioridad
        self.visitado[self.meta] = True

    def bellman_ford_laberinto(self):
        # Iterar n * m - 1 veces para encontrar la ruta mínima
        for _ in range(self.n * self.m - 1):
            for x in range(self.n):  # Iterar sobre las filas del laberinto
                for y in range(self.m):  # Iterar sobre las columnas del laberinto
                    if self.laberinto[x][y] != 1:  # Si la celda no es un obstáculo
                        # Iterar sobre los vecinos de la celda
                        for vecino_x, vecino_y in self.obtener_vecinos(x, y):
                            # La distancia al vecino es la distancia de la celda actual + 1
                            nueva_distancia = self.distancias[x][y] + 1
                            # Si la nueva distancia es menor a la distancia actual del vecino
                            if nueva_distancia < self.distancias[vecino_x][vecino_y]:
                                # Actualizar la distancia del vecino a la nueva distancia
                                self.distancias[vecino_x][vecino_y] = nueva_distancia
                                # Actualizar el padre del vecino a la celda actual
                                self.padres[vecino_x][vecino_y] = (x, y)

        # Verificar si hay ciclos negativos en el laberinto
        for x in range(self.n):
            for y in range(self.m):
                if self.laberinto[x][y] != 1:  # Si la celda no es un obstáculo
                    # Iterar sobre los vecinos de la celda
                    for vecino_x, vecino_y in self.obtener_vecinos(x, y):
                        # Si la distancia de la celda actual + 1 es menor a la distancia del vecino
                        if self.distancias[x][y] + 1 < self.distancias[vecino_x][vecino_y]:
                            print("Hay un ciclo negativo en el laberinto.")
                            return None

        ruta = self.obtener_ruta_minima()
        return ruta

    def obtener_ruta_minima(self):
        ruta = []
        x, y = self.meta
        while (x, y) != self.inicio:  # Iterar desde la meta hasta el inicio
            ruta.append((x, y))  # Agregar la celda actual a la ruta
            if self.padres[x, y] is None:  # Si no hay un padre para la celda actual
                # No se encontró una ruta válida
                return None
            x, y = self.padres[x, y]  # Actualizar la celda actual a su padre
        ruta.append(self.inicio)  # Agregar la celda de inicio a la ruta
        ruta.reverse()  # Invertir la ruta para que vaya desde el inicio hasta la meta
        return ruta

    def obtener_vecinos(self, x, y):
        vecinos = []
        for i in range(4):
            new_x = x + self.dx[i]
            new_y = y + self.dy[i]
            if 0 <= new_x < self.n and 0 <= new_y < self.m:
                vecinos.append((new_x, new_y))
        return vecinos

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
        print("Resolviendo laberinto con Bellman-Ford...")
        inicio_tiempo = time.time()
        mem_usage = memory_profiler.memory_usage()
        ruta_minima = self.bellman_ford_laberinto()

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
        [0, 0, 0],
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

    bellman = Bellman(laberinto_ejemplo, inicio, meta)
    bellman.resolver_laberinto()
