f = open("input5_4.txt", "r")
fo = open("output5.txt", "w")

class Graph:
    def __init__(self, s):
        self.queue = []
        self.visited = [0]*s
        self.parent = [0]*s
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
        self.parent[v-1] = -1
        while self.queue != []:
            for i in self.Adj[self.queue[0]]:
                if self.visited[i-1]==0:
                    self.visited[i-1]=1
                    self.queue.append(i)
                    self.parent[i-1]=self.queue[0]
            self.queue.pop(0)
    
    def Spath(self, s, t):
        self.BFS(s)
        arr = [t]
        now = t-1
        while now!=s-1:
            next = self.parent[now]
            arr.append(next)
            now = next-1
        for i in range(len(arr)//2):
            arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        return arr




fl = f.readline().strip().split(" ")
s = int(fl[0])
n = int(fl[1])
t = int(fl[2])

graph = Graph(s)
for i in range(n):
    cur = f.readline().strip().split(" ")
    v1 = int(cur[0])
    v2 = int(cur[1])
    graph.addEdge(v1, v2)

thepath = graph.Spath(1, t)
txt = ""
for i in thepath:
    txt += f"{i} "

fo.writelines(f"Time: {len(thepath)-1}\n")
fo.writelines(f"Shortest Path: {txt}")

f.close()
fo.close()