def dfs_recursivo(grafo,nodo, visitado=None):
    if visitado is None:
        visitado=set()
    visitado.add(nodo)
    print(nodo, end=" ")
    
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_recursivo(grafo,vecino,visitado)

grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}
           
print("\nRecorrido DFS (recursivo):")
dfs_recursivo(grafo,0)