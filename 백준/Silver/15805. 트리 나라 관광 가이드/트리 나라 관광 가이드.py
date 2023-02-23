num = int(input())
save = [-1 for _ in range(num//2+1)]
plan = list(map(int,input().split()))

for p in range(1, num):
    if p > 1 and plan[p-2] == plan[p]:
        continue
    if save[plan[p-1]] == plan[p]:
        continue
    save[plan[p]] = plan[p-1]

print(num//2+1)
print(*save)