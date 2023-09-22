f = open("input2_4.txt", "r")
fo = open("output2.txt", "w")

memory = {}

def findways(n):
    if n==1 or n==0:
        return 1
    else:
        if n not in memory:
            memory[n] = findways(n-1) + findways(n-2)
        return memory[n]

n = int(f.readline().strip())
gg = findways(n)

fo.writelines(f"{gg}")

f.close()
fo.close()