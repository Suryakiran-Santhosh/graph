
from typing import List, Dict, Set
from collections import deque, defaultdict

class Graph:
    
    def __init__(self):
        self.graph : Dict[int, Set[int]] = defaultdict()
    
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


    def bfs(self, start_node : int) -> List[int]:
        result = []
        q = deque()
        seen = set()

        q.append(start_node)

        while len(q) > 0:
            neighbors = len(q)
            for _ in range(0, neighbors, 1):
                current_vertex = q.popleft()
                if current_vertex not in seen:
                    seen.add(current_vertex)
                    result.append(current_vertex)

                for adjacent_vertex in self.graph[current_vertex]:
                    q.append(adjacent_vertex)

        return result


    def dfs(self, start_node : int) -> List[int]:
        result = []
        stack = deque()
        seen = set()

        stack.append(start_node)

        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex not in seen:
                seen.add(current_vertex)
                result.append(current_vertex)

            for adjacent_vertex in self.graph[current_vertex]:
                if not adjacent_vertex in seen:
                    stack.append(adjacent_vertex)
        
        return result

