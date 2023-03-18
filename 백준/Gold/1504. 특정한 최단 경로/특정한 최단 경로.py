import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    save = [INF] * (N + 1)
    save[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if save[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < save[i[0]]:
                save[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return save


start = dijkstra(1)
v1_road = dijkstra(v1)
v2_road = dijkstra(v2)
answer1 = start[v1] + v1_road[v2] + v2_road[N]
answer2 = start[v2] + v2_road[v1] + v1_road[N]

result = min(answer1, answer2)

if result >= INF:
    print(-1)
else:
    print(result)
