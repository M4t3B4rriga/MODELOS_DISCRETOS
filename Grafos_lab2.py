def nodosGrafos(graph,nodos):
    """
    en esta funcion nos permite mostrar todos los nodos que contiene el grafo
    parametros:graph,nodos
    retona:
    ---------------
    """
    #inicamos una variable 
    i=0
    #recorrido para el grafo
    for dato in graph:
        #imprimimos el grafo
        print("Nodo {}: {}".format(nodos[i],dato))
        #incrementamos la variable para incrementar el nodo
        i+=1

def nodoGrafo(graph,numNodo):
    """
    en esta funcion nos muestra los elementos que contiene el nodo 
    parametro: graph, numNodos
    retorna: graph[]
    """
    #condicion es igual a 1
    if len(graph[numNodo])==1:
        #nos retornana el grafo basio 
        return graph[numNodo][0]
    #retorna el umero del grafo
    return graph[numNodo]

def viasTren(nodos,costos,vias):
    """
    esta funcio nos muetars todas la posibles vias que puede tener 
    parametros: nodos, costos, vias
    retorna:
    ------------------
    """
    #inicio de los costos
    cost=costos[(1,3)]
    #funcion de recorrido por todas las vias
    for i in range(len(vias)): 
        #recorrido por las vias
        for j in vias[i]:
            #imprime las vias
            print("Ruta {}-{}".format(nodos[j[0]], nodos[j[1]]))
            #aumenta el costo
            cost+=costos[(j)]
        #imprimimos el costo    
        print("Costo total de horas: ",cost) 
        print("--------------------------")



if __name__=='__main__':
    #creamos el grafo
    graph, cost=[[]for i in range (4)],{}
    #creacion de los nodos
    nodos=['Estacion_carlos_peligrini','PueyPredon','Facultad_de_medicina_UBA','SantaFe']
     #creacion de los nodos
    Estacion_carlos_peligrini=0
     #creacion de los nodos
    PueyPredon=1
     #creacion de los nodos
    Facultad_de_medicina_UBA=2
     #creacion de los nodos
    SantaFe=3
    #ingresamos los grafos 
    graph[Estacion_carlos_peligrini].append(Estacion_carlos_peligrini)
     #ingresamos los grafos 
    graph[Estacion_carlos_peligrini].append(PueyPredon)
     #ingresamos los grafos 
    graph[Estacion_carlos_peligrini].append(Facultad_de_medicina_UBA)
     #ingresamos los grafos 
    graph[PueyPredon].append(SantaFe)
     #ingresamos los grafos 
    graph[PueyPredon].append(Estacion_carlos_peligrini)
    #creamos los costos de los nodos 
    cost[(Estacion_carlos_peligrini,Estacion_carlos_peligrini)]=0
     #creamos los costos de los nodos 
    cost[(Estacion_carlos_peligrini,PueyPredon)]=1
     #creamos los costos de los nodos 
    cost[(PueyPredon,SantaFe)]=2
     #creamos los costos de los nodos 
    cost[(Estacion_carlos_peligrini,Facultad_de_medicina_UBA)]=3
     #creamos los costos de los nodos 
    cost[(Facultad_de_medicina_UBA,PueyPredon)]=4
    #vias que puede recorrer
    vias=[
        [(Estacion_carlos_peligrini,PueyPredon),(PueyPredon,SantaFe)], 
        [(Estacion_carlos_peligrini,Facultad_de_medicina_UBA)],
        [(PueyPredon,Estacion_carlos_peligrini),(Estacion_carlos_peligrini,PueyPredon),(PueyPredon,SantaFe)]
    ]
    #mandamos los parametros
    viasTren(nodos,cost,vias)


