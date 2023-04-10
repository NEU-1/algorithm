n, s = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = 0
_sum = 0
result = 1e9

while True:
    if _sum >= s:
        result = min(result, end - start)
        _sum -= data[start]
        start += 1
    elif end == n:
        break
    else:
        _sum += data[end]
        end += 1

if result == 1e9:
    print(0)
else:
    print(result)
