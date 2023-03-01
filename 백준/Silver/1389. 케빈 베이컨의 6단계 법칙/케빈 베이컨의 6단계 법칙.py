
from collections import deque

N, M = map(int, input().split())

save = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    save[a].append(b)
    save[b].append(a)

people = []

for i in range(1, N+1):
    jump = [-1 for _ in range(N+1)]
    jump[i] = 0
    queue = deque([i])
    while queue:
        curr = queue.popleft()
        for nxt in save[curr]:
            if jump[nxt] == -1:
                jump[nxt] = jump[curr] + 1
                queue.append(nxt)
    
    people.append(sum(jump[1:]))

print(people.index(min(people)) + 1)
