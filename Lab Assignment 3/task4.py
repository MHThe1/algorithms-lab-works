f = open("input4.txt", "r")
fo = open("output4.txt", "w")

def quickselect(a, l, r, k):
  pivot = a[r]
  p = l
  for i in range(l, r):
    if a[i] <= pivot:
      a[p], a[i] = a[i], a[p]
      p+=1
  a[p], a[r] = a[r], a[p]
  if p == k:
    return(a[p])
  elif p < k:
    return quickselect(a, p+1, r, k)
  else:
    return quickselect(a, l, p-1, k)
  
N = f.readline().strip().split(" ")
n = int(N[0])
arr = f.readline().strip().split(" ")
for i in range(n):
    arr[i] = int(arr[i])
Q = f.readline().strip().split(" ")
q = int(Q[0])
for i in range(q):
    k = int(f.readline().strip())
    r = quickselect(arr, 0, n-1, k-1)
    fo.writelines(f"{r}\n")

f.close()
fo.close()