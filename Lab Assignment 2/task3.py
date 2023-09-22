def merge(a, b):
  n1 = len(a)
  n2 = len(b)
  n = n1 + n2
  farr = [None]*n
  p = 0
  q = 0
  for i in range(n):
      if p<n1 and q<n2 and a[p]<=b[q]:
          farr[i]=a[p]
          p += 1
      elif p<n1 and q<n2 and a[p]>b[q]:
          farr[i]=b[q]
          q += 1
      elif p>=n1 and q<n2:
          farr[i]=b[q]
          q += 1
      elif q>=n2 and p<n1:
          farr[i]=a[p]
          p += 1
  return farr

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)

f = open("input3.txt", "r")
fo = open("output3.txt", "w")
n = int(f.readline().strip())
garr = f.readline().strip().split(" ")
for i in range(n):
  garr[i]=int(garr[i])

sarr = mergeSort(garr)
outtxt = ""
for i in range(len(sarr)):
  if i + 1 < len(sarr):
    outtxt += f"{sarr[i]} "
  else:
    outtxt += f"{sarr[i]}"
fo.writelines(outtxt)

f.close()
fo.close()