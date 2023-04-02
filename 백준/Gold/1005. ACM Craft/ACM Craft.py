import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        in_degree[b] += 1
    W = int(sys.stdin.readline())

    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    result = [0] * (N+1)
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            in_degree[next] -= 1
            result[next] = max(result[next], result[curr]+time[curr])
            if in_degree[next] == 0:
                queue.append(next)

    print(result[W]+time[W])
