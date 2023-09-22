f = open("input2_2.txt", "r")
fo = open("output2.txt", "w")

fl = f.readline().strip().split(" ")
n = int(fl[0])
m = int(fl[1])

arr = [None]*n

for i in range(n):
    curr = f.readline().strip().split(" ")
    a = int(curr[0])
    b = int(curr[1])
    arr[i] = (a, b)

arr.sort(key = lambda y:y[1])

marr = [0]*m
c = 0
done = []

for i in range(len(arr)):
    marr.sort(reverse=True)
    for j in range(m):
        if arr[i][0] >= marr[j] and i not in done:
            marr[j] = arr[i][1]
            done.append(i)
            c+=1

fo.writelines(f"{c}")

f.close()
fo.close()