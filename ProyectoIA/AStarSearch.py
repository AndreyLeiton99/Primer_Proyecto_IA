import heapq
import time
import memory_profiler
from MetodosDeImpresion import imprimir_datos

class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.n = len(grid)
        self.m = len(grid[0])

    def heuristic(self, a, b):
        return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

    def find_path(self):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        close_set = set()
        came_from = {}
        gscore = {self.start: 0}
        fscore = {self.start: self.heuristic(self.start, self.goal)}
        oheap = []
        heapq.heappush(oheap, (fscore[self.start], self.start))

        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == self.goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < len(self.grid):
                    if 0 <= neighbor[1] < len(self.grid[0]):
                        if self.grid[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))

        return False
    
    # Método para resolver el laberinto con A* search y medir el tiempo de ejecución y consumo de memoria
    def resolver_laberinto(self, algoritmo, nombre_laberinto):
        print("Resolviendo laberinto con A* search...")
        inicio_tiempo = time.time()
        mem_usage = memory_profiler.memory_usage()
        ruta_minima = self.find_path()
        mem_usage_end = memory_profiler.memory_usage()
        tiempo_total = time.time() - inicio_tiempo

        imprimir_datos(mem_usage, ruta_minima, mem_usage_end, tiempo_total, self.grid, self.n, self.m, algoritmo, nombre_laberinto)
