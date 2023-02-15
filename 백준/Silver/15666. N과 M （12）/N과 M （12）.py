N, M = map(int, input().split())
save = list(map(int, input().split()))
save.sort()
lst = []
cnt = 0
visited = [False] * (N+1)

def DFS(depth, k):
    prev = 0
    if depth == M:
        print(*lst)
        return
    else:
        for i in range(k, N):
            if save[i] != prev:
                lst.append(save[i])
                prev = save[i]
                visited[i] = True
                DFS(depth + 1, i)
                lst.pop()
                visited[i] = False

DFS(0, 0)