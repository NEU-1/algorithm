import sys
from math import sqrt
from operator import itemgetter

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

def kruskal(graph, parent, rank):
    result = 0

    for weight, a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            result += weight

    return result

def main():
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]

    graph = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            graph.append((distance, i, j))

    graph.sort(key=itemgetter(0))
    parent = [i for i in range(n)]
    rank = [0] * n

    print("%.2f" % kruskal(graph, parent, rank))

if __name__ == "__main__":
    main()
