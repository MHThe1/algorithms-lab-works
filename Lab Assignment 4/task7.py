f = open("input7_3.txt", "r")
fo = open("output7.txt", "w")

class Graph:
    def __init__(self):
        self.visited = []
        self.Adj = {}
    def addEdge(self, v1, v2):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append(v2)
        if v2 not in self.Adj:
            self.Adj[v2] = []
        self.Adj[v2].append(v1)

    def DFS(self, v):
        self.visited.append(v)
        
        far_v = v
        far_d = 0

        for i in self.Adj[v]:
            if i not in self.visited:
                side_v, side_d = self.DFS(i)
                if side_d > far_d:
                    far_v = side_v
                    far_d = side_d
        return far_v, far_d+1

fl = f.readline().strip().split(" ")
s = int(fl[0])

graph = Graph()
curr = f.readline().strip()
while curr != "":
    cur = curr.split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    graph.addEdge(v1, v2)
    curr = f.readline().strip()

A, ad = graph.DFS(1)
graph.visited = []
B, bd = graph.DFS(A)

fo.writelines(f"{A} {B}")


f.close()
fo.close()