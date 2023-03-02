import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

cnt = 0
for i in coin[::-1]:
    if K >= i:
        cnt += K//i
        K %= i
    if K == 0:
        break
print(cnt)