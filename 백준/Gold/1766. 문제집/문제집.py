import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
save = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    save[b] += 1

def top():
    result = []
    que = []

    for i in range(1, n+1):
        if save[i] == 0:
            heapq.heappush(que, i)

    while que:
        cur = heapq.heappop(que)
        result.append(cur)

        for node in graph[cur]:
            save[node] -= 1
            if save[node] == 0:
                heapq.heappush(que, node)

    return result

print(*top())
