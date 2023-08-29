import heapq
import time

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
RESET_COLOR = '\033[0m'

class Dijkstra:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.n = len(laberinto)
        self.m = len(laberinto[0])
        self.distancias = [[float('inf')] * self.m for _ in range(self.n)]
        self.distancias[inicio[0]][inicio[1]] = 0
        self.visitados = [[False] * self.m for _ in range(self.n)]
        self.cola_prioridad = [(0, inicio)]

    def dijkstra_laberinto(self):
        while self.cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(self.cola_prioridad)
            x, y = nodo_actual

            if nodo_actual == self.meta:
                break

            if self.visitados[x][y]:
                continue

            self.visitados[x][y] = True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.n and 0 <= ny < self.m and not self.visitados[nx][ny]:
                    peso = 1 if self.laberinto[nx][ny] == 0 else float('inf')
                    nueva_distancia = distancia_actual + peso

                    if nueva_distancia < self.distancias[nx][ny]:
                        self.distancias[nx][ny] = nueva_distancia
                        heapq.heappush(self.cola_prioridad, (nueva_distancia, (nx, ny)))

        ruta_minima = self.reconstruir_ruta()
        return ruta_minima

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

    def resolver_laberinto_ejemplo(self):
            inicio_tiempo = time.time()
            ruta_minima = self.dijkstra_laberinto()
            tiempo_total = time.time() - inicio_tiempo

            ruta_minima_str = ' -> '.join(f'({x},{y})' for x, y in ruta_minima)

            print("Ruta mínima:", ruta_minima_str)
            print("Tiempo total:", tiempo_total, "segundos")

            print("\nLaberinto con Ruta:")
            self.imprimir_laberinto_con_ruta(ruta_minima)

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

laberinto_solver = Dijkstra(laberinto_ejemplo, inicio_ejemplo, meta_ejemplo)
laberinto_solver.resolver_laberinto_ejemplo()