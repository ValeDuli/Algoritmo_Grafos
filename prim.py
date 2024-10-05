import heapq

def prim(vertices, edges):
    #   Crear una lista de adyacencia
    adj_list={i:[] for i in range(vertices)}
    for u, v, weight in edges:
        adj_list[u].append((weight,v))
        adj_list[v].append((weight,u))
        
    #   Inicializar el MST y el heap
    mst=[]
    visited=[False]*vertices
    min_heap=[(0,0)]    #   (peso, vertice) comenzando desde el vertice 0
    
    while len(mst)<vertices-1:
        weight, u=heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u]=True
        mst.append((weight,u))
        
        for next_weight, v in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_weight, v))
                
    return mst

#   Ejemplo de uso
vertices=7
edges = [
    (0, 1, 7),
    (0, 3, 5),
    (1, 2, 8),
    (1, 3, 9),
    (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15),
    (3, 5, 6),
    (4, 5, 8),
    (4, 6, 9),
    (5, 6, 11)
]

mst=prim(vertices,edges)
print("Aristas del MST:")
total_weight=0
for weight, v in mst:
    total_weight+=weight
    print(f"Peso {weight} al vertices {v}")
print(f"Peso total del MST: {total_weight}")
