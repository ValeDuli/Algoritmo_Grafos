import heapq

def a_star(grafo, inicio, objetivo, heuristica):
    cola=[]
    heapq.heappush(cola,(0,inicio))
    costos={inicio:0}
    padres={inicio: None}
    
    while cola:
        _, nodo_actual=heapq.heappop(cola)
        
        if nodo_actual==objetivo:
            camino=[]
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual=padres[nodo_actual]
            return camino[::-1]
        
        for vecino, costo in grafo[nodo_actual]:
            nuevo_costo= costos[nodo_actual]+costo
            
            if vecino not in costos or nuevo_costo<costos[vecino]:
                costos[vecino]=nuevo_costo
                prioridad=nuevo_costo+heuristica(vecino,objetivo)
                heapq.heappush(cola, (prioridad,vecino))
                padres[vecino]=nodo_actual
                
    return None

#   Ejemplo de grafo y heuristica (distancia Manhattan)
grafo={
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 1), ('E', 6)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 1), ('E', 2)],
    'E': [('B', 6), ('D', 2), ('G', 1)],
    'F': [('C', 2), ('G', 3)],
    'G': [('E', 1), ('F', 3)]
}

def heuristica(nodo, objetivo):
    heuristicas={
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 2,
        'G': 0
    }
    return heuristicas[nodo]

camino=a_star(grafo,'A','G',heuristica)
print(f"Camino encontrado: {camino}")