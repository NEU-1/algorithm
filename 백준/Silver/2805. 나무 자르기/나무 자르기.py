N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
def cut(tree, mid):
    save = 0
    for t in tree:
        if t > mid:
            save += t-mid
    return save

start = 0
end = tree[-1]

while start <= end:
    mid = (start + end) // 2
    if cut(tree, mid) == M:
        print(mid)
        break
    elif cut(tree, mid) > M:
        start = mid + 1
    else:
        end = mid - 1
else:
    print(end)


