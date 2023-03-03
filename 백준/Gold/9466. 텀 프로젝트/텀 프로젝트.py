import sys

sys.setrecursionlimit(10**6)

def dfs(n):
    global count

    visited[n] = True
    project.append(n)

    if visited[save[n]] == True:
        if save[n] in project:
            count -= len(project[project.index(save[n]):])
        return

    else:
        dfs(save[n])

T = int(input())

for _ in range(T):
    N = int(input())

    save = [0]
    save.extend([int(x) for x in sys.stdin.readline().rstrip().split()])

    visited = [False] * (N + 1)
    count = N
    for i in range(1, N + 1):
        if not visited[i]:
            project = []
            dfs(i)

    print(count)