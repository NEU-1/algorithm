N = int(input())
M = 1000000
P = M//10*15
fibonacci = [0, 1]

for i in range(2, P):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    fibonacci[i] %= M

print(fibonacci[N%P])