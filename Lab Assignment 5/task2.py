f = open("input2_3.txt", "r")
fo = open("output2.txt", "w")

class Graph:
    def __init__(self, s):
        self.queue = []
        self.visited = []
        self.adj = {}
        self.size = s

    def addEdge(self, v1, v2):
        if v1 not in self.adj:
            self.adj[v1] = []
        self.adj[v1].append(v2)

    def indeg(self):
        self.indegL = [0]*self.size
        for k in self.adj.keys():
            for v in self.adj[k]:
                self.indegL[v-1] += 1
    
    def DFS(self):
        self.indeg()
        for i in range(len(self.indegL)):
            if self.indegL[i]==0:
                self.queue.append(i+1)
        self.queue.sort()
        for v in self.queue:
            self.DFSin(v)

    def DFSin(self, v):
        self.visited.append(v)
        if v in self.adj:
            newl = sorted(self.adj[v])
            for i in newl:
                self.indegL[i-1] -= 1
                if self.indegL[i-1]==0 and i not in self.visited:
                    self.DFSin(i)

    def checkvalid(self):
        self.DFS()
        if len(self.visited) == self.size:
            return True
        else:
            return False

fl = f.readline().strip().split(" ")
s = int(fl[0])
en = int(fl[1])

graph = Graph(s)
for i in range(en):
    curr = f.readline().strip().split(" ")
    v1 = int(curr[0])
    v2 = int(curr[1])
    graph.addEdge(v1, v2)

outtxt = ""
if graph.checkvalid() == True:
    for i in range(len(graph.visited)):
        if i<len(graph.visited)-1:
            outtxt += f"{graph.visited[i]} "
        else:
            outtxt += f"{graph.visited[i]}\n"
else:
    outtxt = "IMPOSSIBLE"

fo.writelines(outtxt)

f.close()
fo.close()