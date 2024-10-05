def bellman_ford(grafo,inicio):
    #   Distancia inicial a todos los nodos es infinito
    distancias={nodo: float('infinity') for nodo in grafo}
    distancias[inicio]=0    #   Distancia al nodo es 0
    
    #   Relaja las aristas repetidamente
    for _ in range(len(grafo)-1):
        for nodo in grafo:
            for vecino, peso in grafo[nodo].items():
                if distancias[nodo] + peso < distancias[vecino]:
                    distancias[vecino]=distancias[nodo]+peso
                
    #   Comprueba la existencia de ciclos negativos
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            if distancias[nodo]+peso<distancias[vecino]:
                raise ValueError("El grafo contiene un ciclo negativo")
            
    return distancias

#Ejemplo de uso 
grafo={
    'A': {'B':1,'C':4},
    'B': {'A':1,'C':2,'D':5},
    'C': {'A':4,'B':2,'D':1},
    'D': {'B':5,'C':1},
}

distancias=bellman_ford(grafo,'A')
print(f"Distancias desde el nodo 'A': {distancias}")