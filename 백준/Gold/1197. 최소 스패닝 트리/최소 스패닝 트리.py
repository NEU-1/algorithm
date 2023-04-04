def kruskal(graph):
    p = [i for i in range(V+1)]

    def find(i):
        if p[i] == i:
            return i
        p[i] = find(p[i])
        return p[i]
    
    edges = []
    for u in range(V+1):
        for v, w in graph[u]:
            edges.append((u,v,w))
    edges.sort(key=lambda x: x[2])

    total_weight = 0

    for u, v, w in edges:

        x = find(u)
        y = find(v)

        if x != y:
            p[y] = x
            total_weight += w
    return total_weight

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print(kruskal(graph))