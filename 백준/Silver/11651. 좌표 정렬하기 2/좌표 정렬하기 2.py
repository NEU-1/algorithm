import sys
N = int(sys.stdin.readline())
save = []
for n in range(N):
    x, y = map(int, input().split())
    save.append((x,y))
save.sort(key = lambda x: (x[1], x[0]))
for s in save:
    print(*s)