import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = []
        mst = []

        # Start from vertex 0
        heapq.heappush(min_heap, (0, 0, -1))  # (weight, vertex, parent)
        
        while min_heap:
            weight, vertex, parent = heapq.heappop(min_heap)
            if visited[vertex]:
                continue

            visited[vertex] = True
            if parent != -1:
                mst.append((parent, vertex, weight))
            for neighbor, edge_weight in self.graph[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor, vertex))
            
        return mst

# Example Usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 1)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst = g.prim_mst()
print("Edges in the minimum spanning tree:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
