num = int(input())
list_a = []

for i in range(1,num+1):
    a = i//10
    b = i%10
    if a%3 != 0:
        if b == 0:
            list_a.append(i)
        elif b%3 != 0:
            list_a.append(i)
        else:
            list_a.append('-')
    elif a == 0:
        if b%3 == 0:
            list_a.append('-')
        else:
            list_a.append(i)
    elif a%3 == 0:
        if b == 0:
            list_a.append('-')
        elif b%3 != 0:
            list_a.append('-')
        else:
            list_a.append('--')
print(*list_a)