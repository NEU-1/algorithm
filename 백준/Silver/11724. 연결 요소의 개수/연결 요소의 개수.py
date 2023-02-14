import sys

sys.setrecursionlimit(5000)

def check(save, visited, start):
    if visited[start] == True:
        return 0
    else:
        visited[start] = True

    for nxt in save[start]:
        if visited[nxt] == False:
            check(save, visited, nxt)
    return 1





node, T = map(int, input().split())

save = [[] for _ in range(node+1)]
visited = [False] * (node+1)
end = 0

for _ in range(T):
    a, b = map(int, input().split())
    save[a].append(b)
    save[b].append(a)
# print(save)

for n in range(1, node+1):
    # print(check(save, visited, n))
    end += check(save, visited, n)

print(end)