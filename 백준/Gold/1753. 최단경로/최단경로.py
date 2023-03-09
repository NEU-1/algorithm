import heapq

V, E = map(int, input().split())
start = int(input())

graph = {i: [] for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = {i: float('inf') for i in range(1, V+1)}
dist[start] = 0

queue = []
heapq.heappush(queue, (0, start))

while queue:
    now, node = heapq.heappop(queue)

    if dist[node] < now:
        continue

    for neighbor, weight in graph[node]:
        nxt = now + weight

        if nxt < dist[neighbor]:
            dist[neighbor] = nxt
            heapq.heappush(queue, (nxt, neighbor))

# 결과 출력
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])
