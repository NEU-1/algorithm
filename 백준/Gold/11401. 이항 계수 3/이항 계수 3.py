MOD = 1000000007
N, K = map(int, input().split())
 
fact = [1 for _ in range(N+1)]
 
for i in range(2, N+1):
    fact[i] = fact[i-1] * i % MOD

def pow(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (pow(a, b-1) * a) % MOD
    else:
        temp = pow(a, b // 2)
        return (temp * temp) % MOD

A = fact[N]
B = (fact[N-K] * fact[K]) % MOD

print((A % MOD) * (pow(B, MOD - 2) % MOD) % MOD)
