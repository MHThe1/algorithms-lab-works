import heapq

f = open("input1_2.txt", "r")
fo = open("output1.txt", "w")

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
        self.distances = {vertex: float('infinity') for vertex in self.adj}
        self.distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance <= self.distances[current_vertex]:

                for neighbor, weight in self.adj[current_vertex].items():
                    distance = current_distance + weight

                    if distance < self.distances[neighbor]:
                        self.distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

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

source = int(f.readline().strip())
graph.dijkstra(source)

outtxt = ""
for v in graph.distances.values():
    if v!=float('infinity'):
        outtxt += f"{v} "
    else:
        outtxt += f"-1 "

fo.writelines(outtxt)

f.close()
fo.close()
