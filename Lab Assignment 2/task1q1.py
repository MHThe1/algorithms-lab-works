f = open("input1.txt", "r")
fo = open("output1.txt", "w")

fl = f.readline().strip().split(" ")
n = int(fl[0])
target = int(fl[1])

list1 = f.readline().strip().split(" ")
for i in range(n):
    list1[i] = int(list1[i])

flag = False
for i in range(n):
    for j in range(i+1, n):
        if list1[i]+list1[j]==target:
            fo.writelines(f"{i+1} {j+1}")
            flag = True
            break
    if flag==True:
        break
if flag==False:
    fo.writelines("IMPOSSIBLE")

f.close()
fo.close()