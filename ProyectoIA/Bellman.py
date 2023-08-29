

class Bellman:
    def __init__(self, matrix, start_coords, end_coords):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start_coords = start_coords
        self.end_coords = end_coords
    
    def bellman_ford(self):
        distances = [[float('inf')] * self.cols for _ in range(self.rows)]
        distances[self.start_coords[0]][self.start_coords[1]] = 0

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

        # Detectar ciclos negativos
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
                                # Ciclo negativo detectado
                                return "Ciclo negativo detectado"

        shortest_path = []
        r, c = self.end_coords
        while (r, c) != self.start_coords:
            shortest_path.append((r, c))
            neighbors = [
                (r - 1, c), (r + 1, c),
                (r, c - 1), (r, c + 1)
            ]
            for nr, nc in neighbors:
                if 0 <= nr < self.rows and 0 <= nc < self.cols and distances[nr][nc] + self.matrix[r][c] == distances[r][c]:
                    r, c = nr, nc
                    break

        shortest_path.append(self.start_coords)
        shortest_path.reverse()

        return shortest_path

# # Ejemplo de matriz (cambiar los valores según la descripción)
# matrix = [
#     [0, 1, 0, 0, 0],
#     [2, 0, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 3, 0],
#     [0, 0, 0, 0, 1]
# ]

# start_coords = (1, 0)
# end_coords = (3, 3)

# solver = Bellman(matrix, start_coords, end_coords)
# result = solver.bellman_ford()
# if result == "Ciclo negativo detectado":
#     print("Se detectó un ciclo negativo en la matriz.")
# else:
#     print("Ruta mínima:", result)
#     print("Longitud de la ruta:", len(result))
