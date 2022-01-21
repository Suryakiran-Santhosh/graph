

class Graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, vertex : int, neighbor : int) -> None:
        if vertex not in self.graph:
            self.add_vertex(vertex)
        
        if neighbor not in self.graph[vertex]:
            self.graph[vertex].add(neighbor) 
        
    def add_vertex(self, vertex : int) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def display(self) -> None:
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} : {neighbors}")
            
