import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(start, deep, visited):
    visited[start] = True

    for node, m in tree[start]:
        if not visited[node]:
            DFS(node, deep+m, visited)
            save_deep.append(deep+m)
            save_node.append(node)
    return

N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, m = map(int,input().split())
    tree[a].append((b, m))
    tree[b].append((a, m))

visited = [False]*(N+1)
save_deep = []
save_node = []

DFS(1, 0, visited)
if N > 1:
    mx = save_node[save_deep.index(max(save_deep))]

    visited = [False]*(N+1)
    save_deep = []
    DFS(mx, 0, visited)
    print(max(save_deep))
else:
    print(0)

'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 100
6 12 100
'''