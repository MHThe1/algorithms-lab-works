f = open("input3_2.txt", "r")
fo = open("output3.txt", "w")

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x_root = find(parents, x)
    y_root = find(parents, y)

    if x_root != y_root:
        parents[y_root] = x_root

fl = f.readline().strip().split(" ")
n = int(fl[0])
k = int(fl[1])

parents = [0] * (n + 1)
for i in range(1, n + 1):
    parents[i] = i

for i in range(k):
    curr = f.readline().strip().split(" ")
    a = int(curr[0])
    b = int(curr[1])
    union(parents, a, b)
    for j in range(1, n + 1):
        find(parents, j)
    c = parents.count(find(parents, a))
    fo.writelines(f"{c}\n")

f.close()
fo.close()
