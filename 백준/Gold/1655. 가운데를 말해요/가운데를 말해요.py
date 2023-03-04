import sys
import heapq
input = sys.stdin.readline

n = int(input())
left, right = [], []

for i in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        mx = heapq.heappop(left)[1]
        mn = heapq.heappop(right)[1]
        heapq.heappush(left, (-mn, mn))
        heapq.heappush(right, (mx, mx))

    print(left[0][1])
