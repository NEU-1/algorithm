from sys import stdin

T = int(input())
n = int(input())
A = list(map(int, stdin.readline().split()))
m = int(input())
B = list(map(int, stdin.readline().split()))

sum_A = []
sum_B = []

for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        sum_A.append(temp)

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        sum_B.append(temp)

sum_A.sort()
sum_B.sort()
left, right = 0, len(sum_B) - 1
result = 0

while left < len(sum_A) and right >= 0:
    temp_sum = sum_A[left] + sum_B[right]

    if temp_sum == T:
        count_A, count_B = 1, 1
        left += 1
        right -= 1

        while left < len(sum_A) and sum_A[left] == sum_A[left - 1]:
            count_A += 1
            left += 1

        while right >= 0 and sum_B[right] == sum_B[right + 1]:
            count_B += 1
            right -= 1

        result += count_A * count_B

    elif temp_sum < T:
        left += 1

    else:
        right -= 1

print(result)
