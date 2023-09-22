f = open("input1b_3.txt", "r")
fo = open("output1b.txt", "w")

class Graph:
    def __init__(self):
        self.Adj = {}
    def addEdge(self, v1, v2, w):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append((v2, w))

fl = f.readline().strip().split(" ")
s = int(fl[0])
n = int(fl[1])

graph = Graph()
for i in range(n):
    cur = f.readline().strip().split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    w = int(cur[2])
    graph.addEdge(v1, v2, w)

txt = ""
for i in range(s+1):
    if i in graph.Adj:
        txt += f"{i}:"
        for j in range(len(graph.Adj[i])):
            txt += f" {graph.Adj[i][j]}"
    else:
        txt += f"{i}:"
    if i<s:
        txt+=f"\n"

fo.writelines(txt)

f.close()
fo.close()