def compstr(str1, str2):
    i = 0
    flag = True
    str1 = str1.upper()
    str2 = str2.upper()

    while flag != False:
        if i >= len(str1) and i >= len(str2):
            return "Equal"
        elif i >= len(str1):
            return flag
        elif i >= len(str2):
            flag = False
        elif ord(str1[i]) < ord(str2[i]):
            return flag
        elif ord(str1[i]) == ord(str2[i]):
            i += 1
        else:
            flag = False
    return flag

f = open("input4.txt", "r")
fo = open("output4.txt", "w")

n = int(f.readline())
bigarr = [None]*n

for i in range(n):
    bigarr[i] = f.readline().split()

for i in range(len(bigarr)):
    minidx = i
    strval = bigarr[i][0]
    for j in range(i+1, len(bigarr)):
        cstrval = bigarr[j][0]
        
        if compstr(cstrval, strval)==True:
            minidx = j
            strval = cstrval
    
    temp = bigarr[i]
    bigarr[i] = bigarr[minidx]
    bigarr[minidx] = temp


for i in range(0, len(bigarr)-1):
    if bigarr[i][0]==bigarr[i+1][0] and bigarr[i][-1] < bigarr[i+1][-1]:
        bigarr[i], bigarr[i+1] = bigarr[i+1], bigarr[i]

for i in range(len(bigarr)):
    strval = ""
    for j in range(len(bigarr[i])):
        if j+1 < len(bigarr[i]):
            strval += bigarr[i][j] + " "
        else:
            strval += bigarr[i][j]
    if i+1 < n:
        fo.writelines(f"{strval}\n")
    else:
        fo.writelines(f"{strval}")

f.close()
fo.close()