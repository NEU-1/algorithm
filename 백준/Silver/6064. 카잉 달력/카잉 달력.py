import math

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())

    num = M * N // math.gcd(M, N)

    if x > y:
        x, y = y, x
        M, N = N, M
    ans = x

    while ans <= num:
        if (ans - y) % N == 0:
            print(ans)
            break
        ans += M

    else:
        print(-1)
