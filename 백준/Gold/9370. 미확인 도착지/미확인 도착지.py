import heapq
import sys

INF = int(1e9) 

def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

T = int(sys.stdin.readline())

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    candidates = []

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(t):
        candidates.append(int(sys.stdin.readline()))

    distance_start = dijkstra(s, n, graph)
    distance_g = dijkstra(g, n, graph)
    distance_h = dijkstra(h, n, graph)

    candidates.sort()
    for candidate in candidates:
        if distance_start[g] + distance_g[h] + distance_h[candidate] == distance_start[candidate] or \
            distance_start[h] + distance_h[g] + distance_g[candidate] == distance_start[candidate]:
            print(candidate, end=' ')
    print()
