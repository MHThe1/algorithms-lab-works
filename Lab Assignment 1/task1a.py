f = open('input1a.txt', 'r')
fo = open('output1a.txt', 'w')

first_line = f.readline().strip()

T = int(first_line)
for i in range(T):
    current_number = int(f.readline().strip())
    if i+1 != T:
        if current_number%2==0:
            fo.writelines(f"{current_number} is an Even number.\n")
        else:
            fo.writelines(f"{current_number} is an Odd number.\n")
    else:
        if current_number%2==0:
            fo.writelines(f"{current_number} is an Even number.")
        else:
            fo.writelines(f"{current_number} is an Odd number.")
f.close()
fo.close()