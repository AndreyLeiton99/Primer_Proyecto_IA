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
        # Matriz para guardar las distancias de cada celda en el laberinto
        self.distancias = [[float('inf')] * self.m for _ in range(self.n)]
        # La distancia de la celda de inicio a si misma es 0
        self.distancias[inicio[0]][inicio[1]] = 0
        self.visitados = set()  # Conjunto para guardar las celdas visitadas en el laberinto
        # Cola de prioridad para guardar la distancia y la celda actual
        self.cola_prioridad = [(0, inicio)]

    def dijkstra_laberinto(self):
        while self.cola_prioridad:  # Mientras la cola de prioridad no esté vacía
            distancia_actual, nodo_actual = heapq.heappop(
                self.cola_prioridad)  # Obtener la celda con la menor distancia
            x, y = nodo_actual  # Obtener las coordenadas de la celda

            if nodo_actual == self.meta:  # Si la celda actual es la meta
                break  # Terminar el algoritmo

            if nodo_actual in self.visitados:  # Si la celda actual ya fue visitada
                continue  # Continuar con el siguiente nodo

            # Marcar la celda actual como visitada
            self.visitados.add(nodo_actual)

            # Iterar sobre los vecinos de la celda actual
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy  # Obtener las coordenadas del vecino

                # Si el vecino está dentro del laberinto y no es un obstáculo
                if 0 <= nx < self.n and 0 <= ny < self.m and self.laberinto[nx][ny] == 0:
                    # La distancia al vecino es la distancia de la celda actual + 1
                    nueva_distancia = distancia_actual + 1

                    # Si la nueva distancia es menor a la distancia actual del vecino
                    if nueva_distancia < self.distancias[nx][ny]:
                        # el vecino seria parte de la ruta minima, por lo que se agrega a la cola de prioridad con su nueva distancia
                        # Actualizar la distancia del vecino a la nueva distancia
                        self.distancias[nx][ny] = nueva_distancia
                        # Agregar el vecino a la cola de prioridad
                        heapq.heappush(self.cola_prioridad,
                                       (nueva_distancia, (nx, ny)))

        ruta_minima = self.reconstruir_ruta()  # Reconstruir la ruta mínima
        return ruta_minima

    def reconstruir_ruta(self):
        ruta = []
        x, y = self.meta

        while (x, y) != self.inicio:  # Iterar desde la meta hasta el inicio
            ruta.append((x, y))  # Agregar la celda actual a la ruta

            min_dist = float('inf')  # Distancia mínima a la celda actual
            next_x, next_y = x, y  # Coordenadas del siguiente nodo en la ruta mínima

            # Iterar sobre los vecinos de la celda actual
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy  # Obtener las coordenadas del vecino

                if 0 <= nx < self.n and 0 <= ny < self.m:  # Si el vecino está dentro del laberinto
                    # Si la distancia del vecino es menor a la distancia mínima actual,
                    if self.distancias[nx][ny] < min_dist:
                        # el vecino es parte de la ruta mínima y se actualizan las coordenadas del siguiente nodo
                        # Actualizar la distancia mínima
                        min_dist = self.distancias[nx][ny]
                        next_x, next_y = nx, ny  # Actualizar las coordenadas del siguiente nodo

            x, y = next_x, next_y  # Actualizar la celda actual a la siguiente celda en la ruta mínima

        ruta.append(self.inicio)  # Agregar la celda de inicio a la ruta
        ruta.reverse()  # Invertir la ruta para que vaya desde el inicio hasta la meta
        return ruta

    # Imprimir el laberinto con la ruta mínima resaltada en colores
    def imprimir_laberinto_con_ruta(self, ruta):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in ruta:
                    color_index = ruta.index((i, j)) % len(COLORS)
                    print(COLORS[color_index] +
                          str(self.laberinto[i][j]) + RESET_COLOR, end=' ')
                else:
                    print(self.laberinto[i][j], end=' ')
            print()

    # Método para resolver el laberinto con Dijkstra y medir el tiempo de ejecución y consumo de memoria
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
        [0, 1, 0],
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
