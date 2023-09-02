import heapq
import time
import memory_profiler

# Definición de colores para resaltar los caminos en el laberinto
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m',
          '\033[33m', '\033[96m', '\033[35m', '\033[33m', '\033[34m', '\033[95m', '\033[32m']
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
        self.visitados = set()
        self.cola_prioridad = [(0, inicio)]

    def dijkstra_laberinto(self):
        while self.cola_prioridad:
            print(self.cola_prioridad, "\n", self.distancias, "\n", self.visitados)
            distancia_actual, nodo_actual = heapq.heappop(self.cola_prioridad)
            x, y = nodo_actual

            print("Nodo actual:", nodo_actual, "Distancia actual:", distancia_actual)
            if nodo_actual == self.meta:
                break

            print("Vecinos:", [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]])
            if nodo_actual in self.visitados:
                continue

            self.visitados.add(nodo_actual)

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                print("Vecino:", (nx, ny))
                if 0 <= nx < self.n and 0 <= ny < self.m and self.laberinto[nx][ny] == 0:
                    nueva_distancia = distancia_actual + 1
                    print("Nueva distancia:", nueva_distancia)

                    print("Distancia actual:", self.distancias[nx][ny])
                    if nueva_distancia < self.distancias[nx][ny]:
                        self.distancias[nx][ny] = nueva_distancia
                        heapq.heappush(self.cola_prioridad, (nueva_distancia, (nx, ny)))

        ruta_minima = self.reconstruir_ruta()
        print("La ruta mínima corresponde a:", ruta_minima)
        return ruta_minima

    def reconstruir_ruta(self):
        ruta = []
        x, y = self.meta

        while (x, y) != self.inicio:
            ruta.append((x, y))

            min_dist = float('inf')
            next_x, next_y = x, y

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.n and 0 <= ny < self.m:
                    if self.distancias[nx][ny] < min_dist:
                        min_dist = self.distancias[nx][ny]
                        next_x, next_y = nx, ny

            x, y = next_x, next_y

        ruta.append(self.inicio)
        ruta.reverse()
        return ruta

    def imprimir_laberinto_con_ruta(self, ruta):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in ruta:
                    color_index = ruta.index((i, j)) % len(COLORS)
                    print(COLORS[color_index] + str(self.laberinto[i][j]) + RESET_COLOR, end=' ')
                else:
                    print(self.laberinto[i][j], end=' ')
            print()


    def resolver_laberinto(self):
        print("Resolviendo laberinto con Dijkstra...")
        inicio_tiempo = time.time()
        mem_usage = memory_profiler.memory_usage()
        ruta_minima = self.dijkstra_laberinto()
        mem_usage_end = memory_profiler.memory_usage()
        tiempo_total = time.time() - inicio_tiempo

        print("\nTiempo de ejecución:", tiempo_total, "segundos")
        print("Consumo de memoria:", max(mem_usage_end) - max(mem_usage), "MB")

        if ruta_minima:
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
    [2, 1, 3],
    [0, 0, 1],
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

    dijkstra = Dijkstra(laberinto_ejemplo, inicio, meta)
    dijkstra.resolver_laberinto()