import sys
input = sys.stdin.readline

N, R = map(int,input().split())
num = list(map(int,input().split()))
snum = [0]*(N+1)
snum[0] = num[0]
for i in range(1,N+1):
    snum[i] = num[i-1] + snum[i-1]

for _ in range(R):
    a, b = map(int,input().split())
    print(snum[b]-snum[a-1])