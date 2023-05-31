import sys
import heapq

input = sys.stdin.readline

T = int(input().strip())

def dijkstra():
    queue = []
    dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[1][0] = 0
    heapq.heappush(queue, (0, 1, 0))  

    while queue:
        t, here, c = heapq.heappop(queue)

        if dp[here][c] < t:
            continue

        for nh, nc, nt in adj[here]:
            next_cost = nc + c
            next_time = nt + t

            if next_cost > M or dp[nh][next_cost] <= next_time:
                continue

            for i in range(next_cost, M+1):
                if dp[nh][i] > next_time:
                    dp[nh][i] = next_time
                else:
                    break
            heapq.heappush(queue, (next_time, nh, next_cost))
    
    min_time = min(dp[N])
    return -1 if min_time == float('inf') else min_time

for _ in range(T):
    N, M, K = map(int, input().strip().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().strip().split())
        adj[u].append((v, c, d))
    result = dijkstra()
    print(result if result != -1 else "Poor KCM")
