def floyd_warshall(grafo):
    #   Inicializa la matriz de distancias
    distancias={nodo: {nodo: float('infinity') for nodo in grafo} for nodo in grafo}
    for nodo in grafo:
        distancias[nodo][nodo]=0
        for vecino, peso in grafo[nodo].items():
            distancias[nodo][vecino]=peso
    
    #   Actualiza la matriz de distancia
    for k in grafo:
        for i in grafo:
            for j in grafo:
                distancias[i][j]=min(distancias[i][j],distancias[i][k]+distancias[k][j])
                
    return distancias

#   Ejemplo de uso
grafo={
    'A': {'B':1,'C':4},
    'B': {'A':1,'C':2,'D':5},
    'C': {'A':4,'B':2,'D':1},
    'D': {'B':5,'C':1},
}

distancias= floyd_warshall(grafo)
print(f"Matriz de distancias: {distancias}")