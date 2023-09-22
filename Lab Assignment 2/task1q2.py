f = open("input1.txt", "r")
fo = open("output1.txt", "w")

fl = f.readline().strip().split(" ")
n = int(fl[0])
target = int(fl[1])

list1 = f.readline().strip().split(" ")
for i in range(n):
    list1[i] = [int(list1[i]), i]

def mergeSort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    merge(arr, L, R)

def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i][0]<=R[j][0]:
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

def get_targetidx(arr, t):
    mergeSort(arr)
    l = 0
    r = len(arr)-1
    flag = False
    sval = 9999999999
    text = ""
    while l < r:
        if arr[l][0]+arr[r][0] == t:
            flag = True
            if arr[l][1]<arr[r][1] and arr[l][1]<sval:
                text = f"{arr[l][1]+1} {arr[r][1]+1}"
                sval = arr[l][1]
            elif arr[l][1]>arr[r][1] and arr[r][1]<sval:
                text = f"{arr[r][1]+1} {arr[l][1]+1}"
                sval = arr[r][1]
            l += 1
        elif arr[l][0]+arr[r][0] < t:
            l += 1
        else:
            r -= 1
    if flag == False:
        text = "IMPOSSIBLE"
    return text

strval = get_targetidx(list1, target)
fo.writelines(strval)

f.close()
fo.close()