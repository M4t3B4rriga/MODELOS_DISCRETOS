
def proceso():
    """
    Proceso de ingreso de los nodos y matrices e imprecion de las devoluciones de los grafos no dirigidos
    parametros:
    ----------------------
    retorna:
    ----------------------
    """
    # Ingreso del numero de nodos y aristas
    nodo = int(input("Ingrese el numero de nodos: "))
    #ingreso del numero de nodos y aristas 
    arista = int(input("Ingrese el numero de aristas: "))

    # Inicialización de la matriz de adyacencia
    adj_matrix = [[0] * nodo for i in range(arista)]

    # Ingreso de las aristas
    for i in range(arista):
        #ingreso de las aristas 
        u, v = map(int, input("Ingrese la arista {} (en formato 1 2 dependiendo el numero de nodo): ".format(i+1)).split())
        #se adjunta los valores 
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    # Impresión de la matriz de adyacencia
    print("Matriz de adyacencia resultante:")
    #ciclo de repeticion para recorrer la matrix 
    for row in adj_matrix:
        #imprime el resultado
        print(row)


if __name__ == '__main__':
    """
    funcion donde se llama al procesos a realizar 
    parametros:
    -----------------
    retorna:
    ----------------
    """
    #llamamos ala funcion que realiza el proceso 
    proceso()