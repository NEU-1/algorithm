from collections import deque

def bfs(n):
    q = deque()
    q.append((n, [n]))
    while q:
        x, path = q.popleft()
        if x == 1:
            return path
        if x % 3 == 0 and not visited[x//3]:
            visited[x//3] = True
            q.append((x//3, path + [x//3]))
        if x % 2 == 0 and not visited[x//2]:
            visited[x//2] = True
            q.append((x//2, path + [x//2]))
        if not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, path + [x-1]))

n = int(input())
visited = [False] * (n+1)
result = bfs(n)
print(len(result) - 1)
print(" ".join(map(str, result)))
