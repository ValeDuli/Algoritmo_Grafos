def dfs_iterativo(grafo,inicio):
    visitado=set()
    pila=[inicio]
    
    while pila:
        nodo=pila.pop()
        if nodo not in visitado:
            print(nodo, end=" ")
            visitado.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitado:
                    pila.append(vecino)
                    
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}
                    
print("\nRecorrido DFS (iterativo):")
dfs_iterativo(grafo,0)