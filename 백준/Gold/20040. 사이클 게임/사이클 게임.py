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

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

cycle = False
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i + 1)
        break
    else:
        union_parent(parent, a, b)

if not cycle:
    print(0)
