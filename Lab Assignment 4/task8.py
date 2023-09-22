f = open("input8.txt", "r")
fo = open("output8.txt", "w")

class Graph:
    def __init__(self):
        self.color = {}
        self.queue = []
        self.Adj = {}
    def addEdge(self, v1, v2):
        if v1 not in self.Adj:
            self.Adj[v1] = []
        self.Adj[v1].append(v2)
        if v2 not in self.Adj:
            self.Adj[v2] = []
        self.Adj[v2].append(v1)

    def counter(self, v):
        global lyk, vamp
        self.queue.append(v)
        self.color[v] = "black"
        vamp += 1
        while self.queue != []:
            for i in self.Adj[self.queue[0]]:
                if i not in self.color:
                    self.queue.append(i)
                    if self.color[self.queue[0]]=="black":
                        self.color[i]="lime"
                        lyk += 1
                    else:
                        self.color[i]="black"
                        vamp += 1
            self.queue.pop(0)

casen = int(f.readline().strip())
for i in range(casen):
    s = int(f.readline().strip())

    graph = Graph()
    for y in range(s):
        cur = f.readline().strip().split(" ")
        v1 = int(cur[0])
        v2 = int(cur[1])
        graph.addEdge(v1, v2)

    lyk = 0
    vamp = 0
    graph.counter(1)
    fo.writelines(f"Case {i+1}: {max(lyk,vamp)}\n")

f.close()
fo.close()