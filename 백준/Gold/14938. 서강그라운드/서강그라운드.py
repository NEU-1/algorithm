import sys
from heapq import heappop, heappush

def dijkstra(graph, start, M):
    dis = [float('inf')] * len(graph)
    dis[start] = 0
    queue = [(0, start)]

    while queue:
        di, node = heappop(queue)
        if dis[node] < di:
            continue
        for neigh, weight in graph[node]:
            new = di + weight
            if new <= M and new < dis[neigh]:
                dis[neigh] = new
                heappush(queue, (new, neigh))

    return dis


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

mx = 0
for i in range(1, n + 1):
    dis = dijkstra(graph, i, m)
    total = sum(items[j] for j in range(n + 1) if dis[j] != float('inf'))
    mx = max(mx, total)

print(mx)


