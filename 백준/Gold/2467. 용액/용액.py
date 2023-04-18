import sys

n = int(input().strip())
data = list(map(int, input().strip().split()))

data.sort()
left, right = 0, n-1
answer = (data[left], data[right])
min_value = sys.maxsize

while left < right:
    temp = data[left] + data[right]

    if abs(temp) < min_value:
        min_value = abs(temp)
        answer = (data[left], data[right])

    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
