N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

left, right = 1, house[-1] - house[0]
km = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    start = house[0]

    for i in range(1, N):
        if house[i] - start >= mid:
            cnt += 1
            start = house[i]

    if cnt >= C:
        km = mid
        left = mid + 1
    else:
        right = mid - 1

print(km)
