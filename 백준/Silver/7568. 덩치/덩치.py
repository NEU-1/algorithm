N = int(input())
check = list()
count = 0
save = []
for n in range(N):
    age, m = map(int, input().split())
    check.append([age, m])
# print(check)
for one in check:
    for two in check:
        if one[0]<two[0] and one[1]<two[1]:
            count += 1
    save.append(count+1)
    count = 0
print(*save)