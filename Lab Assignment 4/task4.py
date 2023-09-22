f = open("input4_5.txt", "r")
fo = open("output4.txt", "w")

class Graph:
    def __init__(self):
        self.Adj = {}
    def addEdge(self, v1, v2):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append(v2)

    def cDFS(self, v, j):
        global dfsarr
        global b
        dfsarr.append(v)
        if v in self.Adj:
            for i in self.Adj[v]:
                if i == dfsarr[0]:
                    b = True
                if i not in dfsarr:
                    self.cDFS(i, j)

fl = f.readline().strip().split(" ")
s = int(fl[0])
n = int(fl[1])

graph = Graph()
for i in range(n):
    cur = f.readline().strip().split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    graph.addEdge(v1, v2)

nk = len(graph.Adj)

b = False
i = 0
for k in graph.Adj.keys():
    dfsarr = []
    graph.cDFS(k, i)
    i+=1

if b==True:
    fo.writelines("YES")
else:
    fo.writelines("NO")

f.close()
fo.close()