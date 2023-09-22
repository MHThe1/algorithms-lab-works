f = open("input1_3.txt", "r")
fo = open("output1_B.txt", "w")

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
    
    def QFS(self):
        self.indeg()
        for i in range(len(self.indegL)):
            if self.indegL[i]==0:
                self.queue.append(i+1)
    
    def BFS(self):
        self.QFS()
        while self.queue != []:
            v = self.queue[0]
            self.visited.append(self.queue[0])
            if v in self.adj:
                for nv in self.adj[v]:
                    self.indegL[nv-1] -= 1
                    if nv not in self.visited and self.indegL[nv-1]==0:
                        self.queue.append(nv)
            self.queue.pop(0)
    
    def checkvalid(self):
        self.BFS()
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