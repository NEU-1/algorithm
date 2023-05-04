import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

coords = []

for i in range(n):
    x, y, z = map(int, input().split())
    coords.append((x, y, z, i))

for j in range(3):
    coords.sort(key=lambda x: x[j])
    for i in range(1, n):
        dist = abs(coords[i-1][j] - coords[i][j])
        edges.append((dist, coords[i-1][3], coords[i][3]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
