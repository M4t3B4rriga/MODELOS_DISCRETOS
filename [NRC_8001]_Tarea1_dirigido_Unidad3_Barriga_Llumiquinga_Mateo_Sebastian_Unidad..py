
def proceso():
    """
    Se realiza el proceso ingreso y de implrecion de los nodos con las aristas 
    parametros: 
    ------------------------
    retorna:
    -----------------------
    """
    # Pedir número de nodos
    n = int(input("Ingrese el numero de nodos: "))

    # Inicializar lista de adyacencia
    graph = {i: [] for i in range(n)}

    # Pedir número de aristas
    m = int(input("Ingrese el numero de aristas: "))

    # Pedir datos de las aristas
    for i in range(m):
        #pedimos el formato en el que se va a ingresar y guardar
        u, v = map(int, input("Ingrese la arista {} (en formato 1 2 dependiendo el numero de nodo): ".format(i+1)).split())
        #guardamos los valores
        graph[u].append(v)

    # Imprimir grafo
    print("Grafo:")
    #ciclo de repeticion para imprimir los datos
    for u in range(n):
        #imprime los datos
        print("{} -> {}".format(u, graph[u]))

if __name__ == '__main__':
    """
    funcion general 
    parametros:
    -------------
    retorna:
    -------------
    """
    #llamamos al proceso 
    proceso()