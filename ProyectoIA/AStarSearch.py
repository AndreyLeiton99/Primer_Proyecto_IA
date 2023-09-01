import heapq
import time
import memory_profiler
import subprocess

class AStarSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, current, goal):
        # Heurística de distancia Manhattan
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def a_star_search(self, start, end):
        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {}
        g_score = {cell: float('inf') for row in self.grid for cell in row}
        g_score[start] = 0
        f_score = {cell: float('inf') for row in self.grid for cell in row}
        f_score[start] = self.heuristic(start, end)

        while open_list:
            current_f, current = heapq.heappop(open_list)

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = current[0] + dr, current[1] + dc
                neighbor = (nr, nc)

                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != 1:
                    tentative_g_score = g_score[current] + 1

                    if tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, end)
                        if neighbor not in [node[1] for node in open_list]:
                            heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None

# # Ejemplo de matriz (cambiar los valores según la descripción)
# grid = [
#     [0, 1, 0, 0, 0],
#     [2, 0, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 3, 0],
#     [0, 0, 0, 0, 1]
# ]

# start = (1, 0)
# goal = (3, 3)

# solver = AStarSearch(grid)
# path = solver.a_star_search(start, goal)
# print("Ruta mínima:", path)
