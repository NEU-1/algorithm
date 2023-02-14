def check(save, visited, start, cnt):
    visited[start] = True
    for nxt in save[start]:
        if visited[nxt] == False:
            visited[nxt] = True
            cnt += 1
            cnt = check(save, visited, nxt, cnt)

    return cnt


com = int(input())
line = int(input())
save = [[] for _ in range(com+1)]
visited = [False] * (com+1)
cnt = 0

for _ in range(line):
    y, x = map(int,input().split())
    save[y].append(x)
    save[x].append(y)
# print(save)
check = check(save, visited, 1, cnt)
print(check)

# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]