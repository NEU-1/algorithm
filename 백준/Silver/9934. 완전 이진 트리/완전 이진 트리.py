def VLR(n, dps):
    global tmp
    if n > len(building):
        return
    VLR(n*2, dps+1)
    save[dps].append(building[tmp])
    tmp += 1
    VLR(n*2+1, dps+1)


k = int(input())
building = list(map(int,input().split()))

save = [[] for _ in range(k)]
tmp = 0
VLR(1, 0)

for i in save:
    print(*i)