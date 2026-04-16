class Graph:
    def __init__(self):
        # We use a dictionary for the Adjacency List
        self.adj_list = {}

    def add_vertex(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge(self, u, v, weight):
        # Ensure both vertices exist
        self.add_vertex(u)
        self.add_vertex(v)
        # Add the connection (neighbor, weight)
        self.adj_list[u].append((v, weight))

    def get_neighbors(self, u):
        return self.adj_list.get(u, [])

    def get_vertices(self):
        return list(self.adj_list.keys())
