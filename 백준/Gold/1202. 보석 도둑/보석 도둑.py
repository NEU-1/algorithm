import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
ruby = []
for _ in range(N):
    m, v = map(int, input().split())
    ruby.append((m, v))
ruby.sort() 

bags = []
for _ in range(K):
    c = int(input())
    bags.append(c)
bags.sort() 

kg = 0
save = []

j = 0
for bag in bags:
    while j < N and bag >= ruby[j][0]:
        heapq.heappush(save, -ruby[j][1])
        j += 1
    if save:
        kg -= heapq.heappop(save)

print(kg)
