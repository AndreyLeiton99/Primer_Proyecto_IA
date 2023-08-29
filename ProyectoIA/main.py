from ReadCSV import cargar_laberinto, imprimir_laberinto
from Dijkstra import Dijkstra
from Bellman import Bellman
# from memory_profiler import profile

def menu():
    print("\n\n     ≫ Primer proyecto IA ≪\n\n")
    opc = input("Por favor, digite la opcion que desea escoger: \n1- Dijkstra \n2- Bellman \n3- Depht First Search (DFS) \n4- Breadth-First Search (BFS) \n5- A* Search \n\nOpcion: ")
    
    match opc:
        case "1":
            print("Elegiste la opcion 1, Dijkstra\n")
            cargaCSV("Matriz.csv", "1")
            
        case "2":
            print("Elegiste la opcion 2, Bellman\n")
            
            
        case "3":
            print("Elegiste la opcion 3, DFS\n")
        case "4":
            print("Elegiste la opcion 4, BFS\n")
        case "5":
            print("Elegiste la opcion 5, A * Search\n")
        case _:
            print("Opcion incorrecta! Digite nuevamente\n")
            
            
def cargaCSV(nombre_archivo, algoritmo):
    laberinto, inicio, meta = cargar_laberinto(nombre_archivo)
    print("Laberinto Inicial:")
    imprimir_laberinto(laberinto)
    print("\nCoordenadas del punto de inicio:", inicio)
    print("Coordenadas del punto final:", meta)
    
    # este metodo recibe todos los metodos y solo tiene que pasarle a cada uno sus parametros que solicita
    # por ejemplo, "1" es dijkstra
    match algoritmo:
        case "1":
            dijkstra = Dijkstra(laberinto, inicio, meta)
            dijkstra.resolver_laberinto()
        case "2":
            print("hi")
            
        case _:
            print("Incorrecto!")
            

if __name__ == '__main__':    
    menu()