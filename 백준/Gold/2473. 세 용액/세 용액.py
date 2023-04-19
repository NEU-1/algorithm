import sys

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_value = sys.maxsize
result = []

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        temp_sum = arr[i] + arr[left] + arr[right]

        if abs(temp_sum) < abs(min_value):
            min_value = temp_sum
            result = [arr[i], arr[left], arr[right]]

        if temp_sum < 0:
            left += 1
        else:
            right -= 1

print(" ".join(map(str, result)))
