class Grafo:
    def __init__(self):
        self.grafo={}
    
    def agregar_vertice(self,vertice):
        if vertice not in self.grafo:
            self.grafo[vertice]=[]
            
    def agregar_arista(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)   #Para grafos no dirigidos
            
    def imprimir_grafo(self):
        for vertice in self.grafo:
            print(f"Vértice {vertice}: {self.grafo[vertice]}")

#   Ejemplo de uso            
grafo=Grafo()

#   Agregar vértices
for i in range(5):
    grafo.agregar_vertice(i)
    
#   Agregar aristas
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 4)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(1, 4)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)

#   Imprimir grafo
grafo.imprimir_grafo()