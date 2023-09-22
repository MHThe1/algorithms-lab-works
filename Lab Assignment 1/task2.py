def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == False:
            break
        
        """
        Here if a preceding element is larger than it's successor than flag will be set to True, thus if a change happen inside the nested loop the loop will continue.
        If nothing changes inside the nested loop the loop breaks or stops. Thus the loop only runs 1 (constant time) and the nested loop runs n times making the
        best-case scenario θ(n).
        
        """

f = open("input2.txt", "r")
n = int(f.readline())
arr = f.readline().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

bubbleSort(arr)

texto = ""
for i in range(len(arr)):
    if i!=len(arr)-1:
        texto +=f"{arr[i]} "
    else:
        texto += f"{arr[i]}"
fo = open("output2.txt", "w")
fo.writelines(f"{texto}")

f.close()
fo.close()