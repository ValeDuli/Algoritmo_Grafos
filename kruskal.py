class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    
    def find(self, u):
        if self.parent[u]!=u:
            self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        root_u=self.find(u)
        root_v=self.find(v)
        
        if root_u!=root_v:
            if self.rank[root_u]>self.rank[root_v]:
                self.parent[root_v]=root_u
            elif self.rank[root_u]<self.rank[root_v]:
                self.parent[root_u]=root_v
            else:
                self.parent[root_v]=root_u
                self.rank[root_u]+=1
                
def kruskal(vertices, edges):
    uf=UnionFind(vertices)
    mst=[]
    edges=sorted(edges, key=lambda x: x[2])
    
    for u,v, weight in edges:
        if uf.find(u)!=uf.find(v):
            uf.union(u,v)
            mst.append((u,v,weight))
    return mst

#Ejemplo de Uso
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

mst=kruskal(vertices,edges)
print("Aristas del MST:")
for u,v, weight in mst:
    print(f'{u} -- {v} == {weight}')