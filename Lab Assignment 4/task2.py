f = open("input2_4.txt", "r")
fo = open("output2.txt", "w")

class Graph:
    def __init__(self, s):
        self.queue = []
        self.visited = [0]*s
        self.Adj = {}
    def addEdge(self, v1, v2):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append(v2)
        if v2 not in self.Adj:
            self.Adj[v2] = []
        self.Adj[v2].append(v1)

    def BFS(self, v):
        self.queue.append(v)
        self.visited[v-1] = 1

        while self.queue != []:
            fo.writelines(f"{self.queue[0]} ")
            for i in self.Adj[self.queue[0]]:
                if self.visited[i-1]==0:
                    self.visited[i-1]=1
                    self.queue.append(i)
            self.queue.pop(0)


fl = f.readline().strip().split(" ")
s = int(fl[0])
n = int(fl[1])

graph = Graph(s)
for i in range(n):
    cur = f.readline().strip().split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    graph.addEdge(v1, v2)

graph.BFS(1)


f.close()
fo.close()