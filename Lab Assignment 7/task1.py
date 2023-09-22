f = open("input1_3.txt", "r")
fo = open("output1.txt", "w")



n = int(f.readline().strip())
arr = []
for i in range(n):
    curr = f.readline().strip().split(" ")
    s = int(curr[0])
    e = int(curr[1])
    arr.append((s, e))

arr.sort(key=lambda x:x[1])

end = 0
count = 0
txt = ""
for i in arr:
    if end <= i[0]:
        count+=1
        txt += f"{i[0]} {i[1]}\n"
        end = i[1]

fo.writelines(f"{count}\n{txt}")

f.close()
fo.close()
