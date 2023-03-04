import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
heapq.heapify(a)

ans = 0

while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, x + y)
    ans += x + y

print(ans)
