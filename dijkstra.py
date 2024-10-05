import heapq

def dijkstra(grafo, inicio):
    #   Distancia inicial a todos los nodos es infinito
    distancias={nodo: float('infinity') for nodo in grafo}
    distancias[inicio]=0    #   Distancia al nodo inicial es 0
    cola_prioridad=[(0, inicio)]    #   (distancia, nodo)
    
    while cola_prioridad:
        distancia_actual, nodo_actual=heapq.heappop(cola_prioridad)
        
        #   Si la distancia es mayor que la distancia registrada, continuar
        if distancia_actual>distancias[nodo_actual]:
            continue
        
        #   Verifica los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distancia=distancia_actual+peso
            
            #   Solo se registra la distancia si es mas corta
            if distancia< distancias[vecino]:
                distancias[vecino]=distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                
    return distancias

#   Ejemplo de uso
grafo={
    'A': {'B':1,'C':4},
    'B': {'A':1,'C':2,'D':5},
    'C': {'A':4,'B':2,'D':1},
    'D': {'B':5,'C':1},
}

distancias=dijkstra(grafo, 'A')
print(f"Distancias desde el nodo 'A': {distancias}")
    
    