import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(graph, start, end, limit, visited):
    if start == end:
        return True

    visited.add(start)

    for next_node, weight in graph[start]:
        if next_node not in visited and weight >= limit:
            if dfs(graph, next_node, end, limit, visited):
                return True

    return False

def binary_search(graph, start, end, max_weight):
    left = 1
    right = max_weight

    while left <= right:
        mid = (left + right) // 2
        visited = set()

        if dfs(graph, start, end, mid, visited):
            left = mid + 1
        else:
            right = mid - 1

    return right

n, m = map(int, input().split())
graph = defaultdict(list)
max_weight = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())

result = binary_search(graph, start, end, max_weight)

print(result)
