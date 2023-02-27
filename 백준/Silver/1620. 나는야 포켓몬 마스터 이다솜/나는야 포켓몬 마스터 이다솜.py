import sys
input = sys.stdin.readline

N, M = map(int,input().split())
도감 = ['']*(N+1)
for i in range(1,N+1):
    도감[i] = input()
# print(도감)

for j in range(M):
    word = input()
    if word[:-1].isnumeric():
        print(도감[int(word)][:-1])
    else:
        print(도감.index(word))
