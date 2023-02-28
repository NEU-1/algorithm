import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    mn_heap = []
    mx_heap = []
    visited = [False] * n
    for i in range(n):
        word, num = input().split()
        num = int(num)
        if word == 'I':
            heapq.heappush(mn_heap, (num, i))
            heapq.heappush(mx_heap, (-num, i))
        elif word == 'D':
            if len(mn_heap) == 0:
                continue
            if num == 1:
                while mx_heap and visited[mx_heap[0][1]]:
                    heapq.heappop(mx_heap)
                if mx_heap:
                    visited[mx_heap[0][1]] = True
                    heapq.heappop(mx_heap)
            elif num == -1:
                while mn_heap and visited[mn_heap[0][1]]:
                    heapq.heappop(mn_heap)
                if mn_heap:
                    visited[mn_heap[0][1]] = True
                    heapq.heappop(mn_heap)
    while mx_heap and visited[mx_heap[0][1]]:
        heapq.heappop(mx_heap)
    while mn_heap and visited[mn_heap[0][1]]:
        heapq.heappop(mn_heap)
    if len(mn_heap) == 0:
        print("EMPTY")
    else:
        print(-mx_heap[0][0], mn_heap[0][0])
