class Graph:
    def __init__(self):
        self.vertices = 0
        self.adj = []
        self.visited = []

    def create_graph(self):
        self.vertices = int(input("Enter number of intersections (vertices): "))
        self.adj = [[0] * self.vertices for _ in range(self.vertices)]
        self.visited = [False] * self.vertices
        edges = int(input("Enter number of roads (edges): "))
        for k in range(1, edges + 1):
            u, v = map(int, input(f"Enter road {k} (intersection1 intersection2): ").split())
            self.adj[u][v] = 1
            self.adj[v][u] = 1

    def display_graph(self):
        print("\nAdjacency Matrix (Road Network)")
        print("   " + " ".join(str(j) for j in range(self.vertices)))
        for i in range(self.vertices):
            print(f"{i}  " + " ".join(str(x) for x in self.adj[i]))

    def dfs(self, v):
        self.visited[v] = True
        print(v, end=" ")
        for i in range(self.vertices):
            if self.adj[v][i] == 1 and not self.visited[i]:
                self.dfs(i)


print("===== Road Network Exploration (DFS) =====")
city_road = Graph()
city_road.create_graph()
city_road.display_graph()

start = int(input("\nEnter starting intersection: "))
print("DFS Traversal (order of intersections visited): ", end="")
city_road.dfs(start)
print()
