sagag = [0] * 1001
sagag[1] = 1
sagag[2] = 3

for s in range(3, 1001):
    sagag[s] = sagag[s-1] + sagag[s-2]*2

print(sagag[int(input())]%10007)