import sys

input = sys.stdin.readline

def ccw(a, b, c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    op -= (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    if op > 0:
        return 1
    elif op < 0:
        return -1
    else:
        return 0

def is_intersect(x1, x2, y1, y2):
    a = ccw(x1, x2, y1) * ccw(x1, x2, y2)
    b = ccw(y1, y2, x1) * ccw(y1, y2, x2)
    if a == 0 and b == 0:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        return x2 >= y1 and y2 >= x1
    return a <= 0 and b <= 0

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parent[b] = a
        group[a] += group[b]
        group[b] = 0

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
group = [1 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if is_intersect(lines[i][:2], lines[i][2:], lines[j][:2], lines[j][2:]):
            union_parent(i, j)

result_group_count = 0
result_max_group_size = 0

for i in range(n):
    if parent[i] == i:
        result_group_count += 1
        result_max_group_size = max(result_max_group_size, group[i])

print(result_group_count)
print(result_max_group_size)
