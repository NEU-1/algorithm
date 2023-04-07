import sys

input = sys.stdin.readline

def is_parent(parent, x):
    if parent[x] != x:
        parent[x] = is_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = is_parent(parent, a)
    b = is_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
max_cost = 0

for edge in edges:
    cost, a, b = edge
    if is_parent(parent, a) != is_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = max(max_cost, cost)

print(result - max_cost)
