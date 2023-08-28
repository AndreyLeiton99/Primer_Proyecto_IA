import csv


def load_maze_from_csv(filename,  delimiter=';'):
    maze = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            maze_row = [int(cell) for cell in row]
            maze.append(maze_row)
    return maze


def print_maze(maze):
    for row in maze:
        print('  '.join(str(cell) for cell in row))


# Cambia 'laberinto.csv' al nombre de tu archivo CSV
filename = 'Matriz.csv'
maze = load_maze_from_csv(filename)

print("Laberinto cargado desde el archivo:")
print_maze(maze)


