import sys
input = sys.stdin.readline

n = int(input())
save = list(map(int, input().split()))
srt = sorted(list(set(save)))
end = {srt[i]: i for i in range(len(srt))}
# print(end)
for i in save:
    print(end[i], end=' ')
