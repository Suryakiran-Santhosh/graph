

class Disjoint_Set:
    def __init__(self, number_of_vertices : int) -> None:
        self.root = [ i for i in range(0, number_of_vertices, 1) ]
        self.rank = [1 for i in range(0, number_of_vertices, 1) ]
        
    def find(self, v : int) -> int:
        # finds and returns the root node
        if self.root[v] == v:  # the vertex is a root
            return v
        self.root[v] = self.find(self.root[v])  # path compression (changing each vertex to the root)
        return self.root[v]

    def union(self, v1 : int, v2 : int)  -> None:
        # connects the root nodes of v1 and v2 to the node with 
        root_v1  = self.find(v1)
        root_v2  = self.find(v2)
        if root_v1 != root_v2:  # v1 and v2 have different root nodes, if same root then do not need to union
            if self.rank[root_v1] > self.rank[root_v2]:
                self.root[root_v2]  = root_v1
            elif self.rank[root_v1] < self.rank[root_v2]:
                self.root[root_v1]  = root_v2
            else:
                self.root[root_v2] =  root_v1
                self.rank[root_v1] += 1

    def connected(self, v1 : int, v2 : int)  -> bool:
        # returns true if v1 and v2 are connected directly or transitively
        return self.find(v1) == self.find(v2)

    def show(self) -> None:
        print(self.root)
        print(self.rank)