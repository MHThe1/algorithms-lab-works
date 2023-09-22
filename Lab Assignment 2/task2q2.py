def addSortedArrays(sarr1, sarr2):
    n1 = len(sarr1)
    n2 = len(sarr2)
    n = n1 + n2
    farr = [None]*n
    a = 0
    b = 0
    for i in range(n):
        if a<n1 and b<n2 and sarr1[a]<=sarr2[b]:
            farr[i]=sarr1[a]
            a += 1
        elif a<n1 and b<n2 and sarr1[a]>sarr2[b]:
            farr[i]=sarr2[b]
            b += 1
        elif a>=n1 and b<n2:
            farr[i]=sarr2[b]
            b += 1
        elif b>=n2 and a<n1:
            farr[i]=sarr1[a]
            a += 1
    return farr

f = open("input2.txt", "r")
fo = open("output2.txt", "w")

n1 = int(f.readline().strip())
arr1 = f.readline().strip().split(" ")
for i in range(n1):
  arr1[i]=int(arr1[i])

n2 = int(f.readline().strip())
arr2 = f.readline().strip().split(" ")
for i in range(n2):
  arr2[i]=int(arr2[i])

narr = addSortedArrays(arr1, arr2)
outtxt = ""
for i in range(len(narr)):
  if i + 1 < len(narr):
    outtxt += f"{narr[i]} "
  else:
    outtxt += f"{narr[i]}"
fo.writelines(outtxt)

f.close()
fo.close()