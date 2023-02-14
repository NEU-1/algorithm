num = int(input())

사각 = [0] * 1001
사각[1] = 1
사각[2] = 2
for n in range(3,1001):
    사각[n] = 사각[n-1] + 사각[n-2]

print(사각[num]%10007)