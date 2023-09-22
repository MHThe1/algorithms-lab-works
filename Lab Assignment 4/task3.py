f = open("input3_4.txt", "r")
fo = open("output3.txt", "w")

class Graph:
    def __init__(self):
        self.visited = {}
        self.Adj = {}
    def addEdge(self, v1, v2):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append(v2)
        if v2 not in self.Adj:
            self.Adj[v2] = []
        self.Adj[v2].append(v1)

    def DFS(self, v):
        self.visited[v]=1
        fo.writelines(f"{v} ")
        if v in self.Adj:
            for i in self.Adj[v]:
                if i not in self.visited:
                    self.DFS(i)


fl = f.readline().strip().split(" ")
s = int(fl[0])
n = int(fl[1])

graph = Graph()
for i in range(n):
    cur = f.readline().strip().split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    graph.addEdge(v1, v2)

graph.DFS(1)


f.close()
fo.close()