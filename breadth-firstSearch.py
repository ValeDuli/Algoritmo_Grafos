from collections import deque

def bfs(grafo, inicio):
    visitado=set()
    cola=deque([inicio])
    visitado.add(inicio)
    
    while cola:
        nodo=cola.popleft()
        print(nodo,end=" ")
        
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)
                
# Ejemplo de uso
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

print("Recorrido BFS")
bfs(grafo,0)