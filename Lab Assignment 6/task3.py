import heapq

f = open("input3_2.txt", "r")
fo = open("output3.txt", "w")

class Graph:
    def __init__(self, s):
        self.queue = []
        self.visited = []
        self.adj = {}
        self.size = s
        for i in range(s):
            self.adj[i+1] = {}

    def addEdge(self, v1, v2, w):
        self.adj[v1][v2] = w

    def dijkstra(self, source):
        self.dangers = {vertex: float('infinity') for vertex in self.adj}
        self.dangers[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_danger, current_vertex = heapq.heappop(priority_queue)

            if current_danger <= self.dangers[current_vertex]:

                for neighbor, danger in self.adj[current_vertex].items():

                    if danger < self.dangers[neighbor] and danger >= current_danger:
                        self.dangers[neighbor] = danger
                        heapq.heappush(priority_queue, (danger, neighbor))
                    elif danger < self.dangers[neighbor] and danger < current_danger:
                        self.dangers[neighbor] = current_danger
                        heapq.heappush(priority_queue, (danger, neighbor))

fl = f.readline().strip().split(" ")
s = int(fl[0])
en = int(fl[1])

graph = Graph(s)
for i in range(en):
    curr = f.readline().strip().split(" ")
    v1 = int(curr[0])
    v2 = int(curr[1])
    w = int(curr[2])
    graph.addEdge(v1, v2, w)

graph.dijkstra(1)

fo.writelines(f"{graph.dangers[s]}")

f.close()
fo.close()
