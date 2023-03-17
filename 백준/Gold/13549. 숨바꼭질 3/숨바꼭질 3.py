from collections import deque

N, K = map(int, input().split())

visited = [-1] * 100001

q = deque()
q.append(N)
visited[N] = 0

while q:
    x = q.popleft()
    if x*2 <= 100000 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.appendleft(x*2)
    if x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
    if x-1 >= 0 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)

print(visited[K])
