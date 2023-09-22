def maxFinder(arr, l, r):
  n=r-l
  if n==0:
    return arr[l]
  elif n==1:
    if arr[l]>=arr[r]:
        return arr[l]
    else:
        return arr[r]
  elif n>1:
    m = (l+r)//2
    Lm = maxFinder(arr, l, m)
    Rm = maxFinder(arr, m+1, r)
    if Lm >= Rm:
      return Lm
    else:
      return Rm

f = open("input4.txt", "r")
fo = open("output4.txt", "w")
n = int(f.readline().strip())
garr = f.readline().strip().split(" ")
for i in range(n):
  garr[i]=int(garr[i])

max = maxFinder(garr, 0, len(garr)-1)
fo.writelines(f"{max}")

f.close()
fo.close()

#The time complexity of my code is O(n)