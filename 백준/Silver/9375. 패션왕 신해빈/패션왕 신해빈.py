import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())
    clothes = dict()
    for _ in range(num):
        _, types = input().split()
        if types not in clothes:
            clothes[types] = 1
        else:
            clothes[types] += 1

    answer = 1
    for cnt in clothes.values():
        answer *= cnt + 1
    print(answer - 1)
