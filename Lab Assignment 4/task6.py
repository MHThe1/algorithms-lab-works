f = open("input6_7.txt", "r")
fo = open("output6.txt", "w")

fl = f.readline().strip().split(" ")
r = int(fl[0])
c = int(fl[1])
mat = [[0]*c for i in range(r)]

for i in range(r):
    curr = f.readline().strip()
    for k in range(c):
        mat[i][k] = curr[k]

def Dcounter(sr, sc):
    global count
    if 0<= sr < r and 0 <= sc < c and (this[sr][sc] == "." or this[sr][sc] == "D") and this[sr][sc] != "V":
        if this[sr][sc]=="D":
            count+=1
        this[sr][sc] = "V"
        Dcounter(sr+1, sc)
        Dcounter(sr-1, sc)
        Dcounter(sr, sc+1)
        Dcounter(sr, sc-1)

max = -1
for i in range(r):
    for j in range(c):
        count = 0
        this = mat.copy()
        Dcounter(i, j)
        if count > max:
            max = count

fo.writelines(f"{max}")

f.close()
fo.close()
