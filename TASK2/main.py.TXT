from graph import Graph
from dijkstra import dijkstra

# 1. Initialize the Graph
g = Graph()

# 2. Add edges (Source, Destination, Weight) based on your study
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'E', 7)
g.add_edge('C', 'E', 8)

# 3. Run Dijkstra's from starting node 'A'
distances, predecessors = dijkstra(g, 'A')

# 4. Print Results
print("Shortest distances from A:")
for node, dist in distances.items():
    print(f"To {node}: {dist}")
