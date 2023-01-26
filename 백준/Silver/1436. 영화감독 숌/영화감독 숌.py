num = int(input())

save = []
count = 0
for n in range(100000000):
    if '666' in str(n):
        save.append(n)
        count += 1
        # print(n)
        if count == num:
            break
print(save[-1])