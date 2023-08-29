

class Bellman:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
    
    def bellman_ford(self, start_coords, end_coords):
        distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        distances[start_coords[0]][start_coords[1]] = 0

        for _ in range(self.rows * self.cols - 1):
            for r in range(self.rows):
                for c in range(self.cols):
                    if self.matrix[r][c] == 1:
                        continue

                    neighbors = [
                        (r - 1, c), (r + 1, c),
                        (r, c - 1), (r, c + 1)
                    ]

                    for nr, nc in neighbors:
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.matrix[nr][nc] != 1 and distances[r][c] + self.matrix[nr][nc] < distances[nr][nc]:
                                distances[nr][nc] = distances[r][c] + self.matrix[nr][nc]

        shortest_path = []
        r, c = end_coords
        while (r, c) != start_coords:
            shortest_path.append((r, c))
            neighbors = [
                (r - 1, c), (r + 1, c),
                (r, c - 1), (r, c + 1)
            ]
            for nr, nc in neighbors:
                if 0 <= nr < self.rows and 0 <= nc < self.cols and distances[nr][nc] + self.matrix[r][c] == distances[r][c]:
                    r, c = nr, nc
                    break

        shortest_path.append(start_coords)
        shortest_path.reverse()

        return shortest_path

# # Ejemplo de matriz (cambiar los valores según la descripción)
# matrix = [
#     [0, 0, 0, 0],
#     [0, 1, 0, 1],
#     [2, 0, 0, 0],
#     [1, 1, 0, 3]
# ]

# start_coords = (2, 0)
# end_coords = (3, 3)

# solver = Bellman(matrix)
# shortest_path = solver.bellman_ford(start_coords, end_coords)
# print("Ruta mínima:", shortest_path)
# print("Longitud de la ruta:", len(shortest_path))
