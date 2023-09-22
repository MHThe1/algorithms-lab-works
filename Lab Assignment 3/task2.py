f = open("input2.txt", "r")
fo = open("output2.txt", "w")

def get_max(A):
    n = len(A)

    if n == 1:
        return float('-inf')
    if n == 2:
        return A[0] + A[1]*A[1]

    left_max = get_max(A[0:n//2])

    right_max = get_max(A[n//2:n])


    lm = -999999999
    for i in range(0,n//2):
      if A[i] > lm:
        lm = A[i]
    rm = 0
    for i in range(n//2,n):
      if abs(A[i]) > rm:
        rm = abs(A[i])
    cross_max = lm + (rm*rm)

    return max(cross_max, left_max, right_max)

n = int(f.readline().strip())
arr = f.readline().strip().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

maxv = get_max(arr)
fo.writelines(f"{maxv}")

f.close()
fo.close()