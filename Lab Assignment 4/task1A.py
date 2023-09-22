import numpy as np

f = open("input1a_1.txt", "r")
fo = open("output1a.txt", "w")

fl = f.readline().strip().split(" ")
dim = int(fl[0])+1
mat = np.zeros((dim, dim), dtype=int)
n = int(fl[1])

for i in range(n):
    curr = f.readline().strip().split(" ")
    mat[int(curr[0])][int(curr[1])] = int(curr[2])

txt = ""
for i in range(len(mat)):
    for j in range(len(mat)):
        if j<len(mat)-1:
            txt += f"{mat[i][j]} "
        else:
            txt += f"{mat[i][j]}\n"

fo.writelines(txt)

f.close()
fo.close()
