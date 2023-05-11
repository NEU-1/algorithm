import sys
input = sys.stdin.readline

def getParent(x):
    if x == parent[x]:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

directions = {'D': (0, 1), 'L': (-1, 0), 'R': (1, 0), 'U': (0, -1)}

N, M = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]
parent = [i for i in range(N * M)]

for num in range(N * M):
    x, y = num % M, num // M
    dx, dy = directions[field[y][x]]
    nx, ny = x + dx, y + dy

    if 0 <= nx < M and 0 <= ny < N:
        next_num = ny * M + nx
        unionParent(num, next_num)

answer = 0
visited = set()
for i in range(N * M):
    parent_i = getParent(parent[i])
    if parent_i not in visited:
        answer += 1
        visited.add(parent_i)

print(answer)
