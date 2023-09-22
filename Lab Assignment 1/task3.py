def sortIdMarks(idarr, marr):
    ht = [None]*len(marr)
    for i in range(len(ht)):
        ht[i]=[marr[i], idarr[i]]
    for i in range(len(ht)):
        maxidx = i
        for j in range(i, len(ht)):
            if ht[j][0]>ht[maxidx][0] or (ht[j][0]==ht[maxidx][0] and ht[j][1]<ht[maxidx][1]):
                maxidx = j

        temp = ht[i]
        ht[i]=ht[maxidx]
        ht[maxidx]=temp
    return ht

f = open("input3.txt", "r")

n = int(f.readline())

idarr = f.readline().split()
marksarr = f.readline().split()

for i in range(len(idarr)):
    idarr[i]=int(idarr[i])
for i in range(len(marksarr)):
    marksarr[i]=int(marksarr[i])

table = sortIdMarks(idarr, marksarr)
       
fo = open("output3.txt", "w")
for i in range(len(table)):
    if i+1<len(table):
        fo.writelines(f"ID: {table[i][1]} Mark: {table[i][0]}\n")
    else:
        fo.writelines(f"ID: {table[i][1]} Mark: {table[i][0]}")

f.close()
fo.close()