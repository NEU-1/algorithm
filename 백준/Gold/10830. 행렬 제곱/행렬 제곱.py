import sys

def matrix_mul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= 1000
    return C

def matrix_pow(A, B):
    if B == 1:
        return A
    if B % 2 == 0:
        tmp = matrix_pow(A, B//2)
        return matrix_mul(tmp, tmp)
    else:
        tmp = matrix_pow(A, B-1)
        return matrix_mul(tmp, A)

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = matrix_pow(A, B)

for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=" ")
    print()
