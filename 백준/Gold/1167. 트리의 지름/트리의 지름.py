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
    info = list(map(int,input().split()))
    a = info [0]
    info = info[1:]
    for j in range(0,len(info)-1,2):
        tree[a].append((info[j], info[j+1]))
        tree[info[j]].append((a, info[j+1]))

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
