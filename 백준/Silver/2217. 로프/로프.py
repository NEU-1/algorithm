n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

mx = 0
for i in range(n):
    t = num[i] * (n - i)
    mx = max(mx, t)

print(mx)
