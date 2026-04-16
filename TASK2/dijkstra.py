import heapq

def dijkstra(graph, start_node):
    # Initialize distances as infinity
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start_node] = 0
    
    # Priority Queue: stores (distance, vertex)
    pq = [(0, start_node)]
    
    # To keep track of the path
    predecessors = {vertex: None for vertex in graph.get_vertices()}

    while pq:
        current_distance, u = heapq.heappop(pq)

        # "Lazy removal" check: skip if we found a better path already
        if current_distance > distances[u]:
            continue

        for neighbor, weight in graph.get_neighbors(u):
            distance = current_distance + weight

            # If this path is shorter, update it!
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = u
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors
