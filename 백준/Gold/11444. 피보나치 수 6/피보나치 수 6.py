def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        c = a + b
        a, b = b, c

    return b

def fib_mod(n):
    if n == 0:
        return 0

    a = [[1, 1], [1, 0]]
    b = [[1, 0], [0, 1]]

    while n > 0:
        if n % 2 == 1:
            b = 행렬(b, a)
        a = 행렬(a, a)
        n //= 2

    return b[0][1] % 1000000007

def 행렬(a, b):
    c = [[0] * len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= 1000000007

    return c

n = int(input())
print(fib_mod(n))
