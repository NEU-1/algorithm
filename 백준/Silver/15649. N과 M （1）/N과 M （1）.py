
def DFS(cnt):
    if cnt == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            DFS(cnt+1)
            visited[i] = False
            result.pop()

N, M = map(int, input().split())
visited = [False] * (N + 1)
result = []

DFS(0)