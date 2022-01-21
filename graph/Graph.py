

class Graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, start : int, end : int) -> None:
        if start not in self.graph:
            self.add_vertex(start)
        
        if end not in self.graph[start]:
            self.graph[start].add(end) 
        
    def add_vertex(self, vertex : int) -> None:
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def display(self) -> None:
        for key, value in self.graph.items():
            print(f"{key} : {value}")
