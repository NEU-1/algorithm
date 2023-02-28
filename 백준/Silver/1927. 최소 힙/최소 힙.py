import sys
input = sys.stdin.readline
import heapq

num = int(input())
hip = []
for _ in range(num):
    n = int(input())
    if n != 0:
        heapq.heappush(hip,n)
    elif n == 0:
        if len(hip) == 0:
            print(0)
        else:
            print(heapq.heappop(hip))