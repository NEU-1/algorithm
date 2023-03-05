import sys
import heapq
input = sys.stdin.readline

n = int(input())
stop = []
for _ in range(n):
    truck, oil = map(int, input().split())
    heapq.heappush(stop, (truck, oil))

L, P = map(int, input().split())

heap = []
cnt = 0
oil = P

while oil < L:
    while stop and stop[0][0] <= oil:
        truck, additional_fuel = heapq.heappop(stop)
        heapq.heappush(heap, -additional_fuel)

    if not heap:
        break

    oil += -heapq.heappop(heap)
    cnt += 1

if oil < L:
    print(-1)
else:
    print(cnt)
