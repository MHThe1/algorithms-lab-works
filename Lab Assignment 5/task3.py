f = open("input3_3.txt", "r")
fo = open("output3.txt", "w")

class Graph:
    def __init__(self, s):
        self.queue = []
        self.visited = []
        self.adj = {}
        self.size = s
        for i in range(s):
            self.adj[i+1] = []

        self.stack = []

    def addEdge(self, v1, v2):
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
        if self.queue == []:
            self.queue = [1]
        for v in self.queue:
            self.DFSin(v)

    def DFSin(self, v):
        self.visited.append(v)
        if v in self.adj:
            for i in self.adj[v]:
                if i not in self.visited:
                    self.DFSin(i)
        self.stack.append(v)

    def revG(self):
        self.revadj = {}
        for i in self.adj.keys():
            for v in self.adj[i]:
                if v not in self.revadj:
                    self.revadj[v] = []
                self.revadj[v].append(i)

    def DFScc(self, v):
        self.visited.append(v)
        self.sccl.append(v)
        if v in self.revadj:
            for i in self.revadj[v]:
                if i not in self.visited and i not in self.sccl:
                    self.DFScc(i)
    
    def SCC(self):
        self.DFS()
        self.revG()
        self.stack.reverse()
        self.visited = []
        while self.stack != []:
            self.sccl = []
            if self.stack[0] in self.visited:
                self.stack.pop(0)
            else:
                self.DFScc(self.stack[0])
                self.stack.pop(0)
                outtxt = ""
                for i in range(len(self.sccl)):
                    if i<len(self.sccl)-1:
                        outtxt += f"{self.sccl[i]} "
                    else:
                        outtxt += f"{self.sccl[i]}\n"
                fo.writelines(outtxt)

        
    

fl = f.readline().strip().split(" ")
s = int(fl[0])
en = int(fl[1])

graph = Graph(s)
for i in range(en):
    curr = f.readline().strip().split(" ")
    v1 = int(curr[0])
    v2 = int(curr[1])
    graph.addEdge(v1, v2)

graph.SCC()

f.close()
fo.close()