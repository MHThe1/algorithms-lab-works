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

n = n1+n2
farr = [None]*n
for i in range(n1):
  farr[i]=arr1[i]
j=n1
for i in range(n2):
  farr[j]=arr2[i]
  j+=1

def isort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    isort(L)
    isort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i]<=R[j]:
        arr[k]=L[i]
        i+=1
      else:
        arr[k]=R[j]
        j+=1
      k+=1
    while i < len(L):
      arr[k]=L[i]
      i+=1
      k+=1
    while j < len(R):
      arr[k]=R[j]
      j+=1
      k+=1

isort(farr)
outtxt = ""
for i in range(len(farr)):
  if i + 1 < len(farr):
    outtxt += f"{farr[i]} "
  else:
    outtxt += f"{farr[i]}"

fo.writelines(outtxt)

f.close()
fo.close()