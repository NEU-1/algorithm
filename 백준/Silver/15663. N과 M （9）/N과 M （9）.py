N, M = map(int, input().split())
save = list(map(int, input().split()))
save.sort()
lst = []
cnt = 0
visited = [False] * (N+1)

def DFS(depth):
    prev = 0
    if depth == M:
        print(*lst)
        return
    else:
        for i in range(N):
            if save[i] != prev and visited[i] == False:
                lst.append(save[i])
                prev = save[i]
                visited[i] = True
                DFS(depth + 1)
                lst.pop()
                visited[i] = False

DFS(0)