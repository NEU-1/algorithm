import sys
input = sys.stdin.readline

def check(n):
    visited = [True] * (n+1)
    visited[0], visited[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if visited[i]:
            for j in range(i*2, n+1, i):
                visited[j] = False
    return [i for i in range(2, n+1) if visited[i]]

primes = set(check(1000000))

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if i in primes and n-i in primes:
            print(n, "=", i, "+", n-i)
            break
