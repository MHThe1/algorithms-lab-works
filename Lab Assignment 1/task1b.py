f = open("input1b.txt", 'r')
fo = open('output1b.txt', 'w')

N = int(f.readline().strip())

for i in range(N):
    cstr = f.readline().strip()
    cstr = cstr.split(' ')

    first_num = int(cstr[1])

    opr = cstr[2]

    sec_num = int(cstr[3])

    if opr=='+':
        r = first_num + sec_num
    elif opr=='-':
        r = first_num - sec_num
    elif opr=='*':
        r = first_num * sec_num
    elif opr=='/':
        r = first_num / sec_num

    if i+1 != N:
        fo.writelines(f"The reasult of {first_num} {opr} {sec_num} is {r}\n")
    else:
        fo.writelines(f"The reasult of {first_num} {opr} {sec_num} is {r}")

f.close()
fo.close()