num = [0] * 12
num[1] = 1
num[2] = 2
num[3] = 4

for n in range(4, 12):
    num[n] = num[n-1] + num[n-2] + num[n-3]

for _ in range(int(input())):
    print(num[int(input())])