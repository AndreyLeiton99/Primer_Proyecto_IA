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
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[33m', '\033[96m'
          , '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
RESET_COLOR = '\033[0m'

class Bellman:

    dx = [-1, 1, 0, 0]  # Movimientos en x, arriba y abajo, no se puede mover en diagonal
    dy = [0, 0, -1, 1]  # Movimientos en y, izquierda y derecha, no se puede mover en diagonal
    
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = np.array(laberinto)
        self.inicio = inicio
        self.meta = meta
        self.n, self.m = self.laberinto.shape
        self.distancias = np.full((self.n, self.m), float('inf'))
        self.distancias[inicio] = 0
        self.padres = np.empty((self.n, self.m), dtype=object)
        self.visitado = np.zeros_like(self.laberinto, dtype=bool)
        self.visitado[self.meta] = True  # Marcar la celda de meta como visitada


    def bellman_ford_laberinto(self):
        for _ in range(self.n * self.m - 1):
            for x in range(self.n):
                for y in range(self.m):
                    if self.laberinto[x][y] != 1:
                        for vecino_x, vecino_y in self.obtener_vecinos(x, y):
                            nueva_distancia = self.distancias[x][y] + 1
                            if nueva_distancia < self.distancias[vecino_x][vecino_y]:
                                self.distancias[vecino_x][vecino_y] = nueva_distancia
                                self.padres[vecino_x][vecino_y] = (x, y)

        for x in range(self.n):
            for y in range(self.m):
                if self.laberinto[x][y] != 1:
                    for vecino_x, vecino_y in self.obtener_vecinos(x, y):
                        if self.distancias[x][y] + 1 < self.distancias[vecino_x][vecino_y]:
                            print("Hay un ciclo negativo en el laberinto.")
                            return None

        ruta = self.obtener_ruta_minima()
        return ruta
    
    def obtener_ruta_minima(self):
        ruta = []
        x, y = self.meta
        while (x, y) != self.inicio:
            ruta.append((x, y))
            if self.padres[x, y] is None:
                # No se encontró una ruta válida, detener la construcción de la ruta
                return None
            x, y = self.padres[x, y]
        ruta.append(self.inicio)
        ruta.reverse()
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
                    print(COLORS[color_index] + str(self.laberinto[i, j]) + RESET_COLOR, end=' ')
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
