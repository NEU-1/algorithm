import sys
sys.setrecursionlimit(10**6)

def check(n):
    for i in save[n]:
        if not visited[i]:
            parents[i] = n 
            visited[n] = True
            check(i)

save = [[] for _ in range(100001)]
num = int(sys.stdin.readline())

for i in range(num - 1):
    a, b = map(int, input().split())
    save[a].append(b) 
    save[b].append(a)

parents = [0]*(num + 1)
visited = [False]*(num + 1)
visited[1] = True
check(1)

for i in range(2, num + 1):
    print(parents[i])
