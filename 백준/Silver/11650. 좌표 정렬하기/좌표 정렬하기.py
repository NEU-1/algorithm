N = int(input())
save = []
for _ in range(N):
    save.append(tuple(map(int,input().split())))
save.sort()
for s in save:
    print(*s)