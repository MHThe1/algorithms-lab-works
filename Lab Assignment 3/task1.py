f = open("input1.txt", "r")
fo = open("output1.txt", "w")

def invm(arr, larr, rarr):
    i = j = k = inv = 0
    while i<len(larr) and j < len(rarr):
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i+=1
        else:
            arr[k] = rarr[j]
            j+=1
            inv += len(larr)-i
        k+=1
    while i<len(larr):
        arr[k]=larr[i]
        i+=1
        k+=1
    while j<len(rarr):
        arr[k]=rarr[j]
        j+=1
        k+=1
    return inv

def invc(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr)//2
    larr = arr[:mid]
    rarr = arr[mid:]
    invl = invc(larr)
    invr = invc(rarr)
    invmc = invm(arr, larr, rarr)
    return invl + invr + invmc

n = int(f.readline().strip())
aliens = f.readline().strip().split(" ")
for i in range(n):
    aliens[i] = int(aliens[i])

print(aliens)
inv_count = invc(aliens)

fo.writelines(f"{inv_count}")

f.close()
fo.close()
