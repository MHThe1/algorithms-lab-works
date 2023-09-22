f = open("input1_2.txt", "r")
fo = open("output1.txt", "w")

class Graph:
    def __init__(self, s):
        self.size = s
        self.adj = []
    
    def addEdge(self, v1, v2, w):
        self.adj.append([v1, v2, w])
    
    def find(self, parent, item):
        if parent[item-1] == item:
            return item
        else:
            return self.find(parent, parent[item-1])
    
    def union(self, parent, set1, set2):
        root1 = self.find(parent, set1)
        root2 = self.find(parent, set2)
        parent[root1-1] = root2

    def kruskal(self):
        parent = []
        self.cost = 0

        for p in range(1, self.size+1):
            parent.append(p)

        self.adj.sort(key=lambda x:x[2])

        i = 0
        e = 0

        while e < self.size-1:
            v1, v2, w = self.adj[i]
            i += 1
            root1 = self.find(parent, v1)
            root2 = self.find(parent, v2)
            
            if root1 != root2:
                e += 1
                self.cost += w
                self.union(parent, v1, v2)
        

fl = f.readline().strip().split(" ")
s = int(fl[0])
lt = int(fl[1])

graph = Graph(s)
for i in range(lt):
    curr = f.readline().strip().split(" ")
    v1 = int(curr[0])
    v2 = int(curr[1])
    w = int(curr[2])
    graph.addEdge(v1, v2, w)

graph.kruskal()

fo.writelines(f"{graph.cost}")

f.close()
fo.close()