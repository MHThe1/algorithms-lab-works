f = open("input3.txt", "r")
fo = open("output3.txt", "w")

def QuickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

n = int(f.readline().strip())
arr = f.readline().strip().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

QuickSort(arr, 0, n-1)
out_txt = ""
for i in range(n):
    if i+1==n:
        out_txt += f"{arr[i]}\n"
    else:
        out_txt += f"{arr[i]} "
fo.writelines(out_txt)

f.close()
fo.close()