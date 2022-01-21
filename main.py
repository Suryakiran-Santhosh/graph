import graph.Graph as Graph

def main():
    graph = Graph.Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 7)
    graph.add_edge(4, 8)
    graph.add_edge(4, 6)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 9)
    graph.add_edge(9, 8)
    graph.add_vertex(8)
    graph.add_vertex(7)
    graph.display()
    print(f"DFS Traversal: {graph.dfs(1)}")
    print(f"BFS Traversal: {graph.bfs(1)}")



if __name__ == "__main__":
    main()