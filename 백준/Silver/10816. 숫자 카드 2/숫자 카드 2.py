import sys

def card_count(start, end, card, c):
    while start <= end:
        mid = (start+end)//2
        if c == card[mid]:
            return card[start:end+1].count(c)
        elif c > card[mid]:
            start = mid+1
        else:
            end = mid-1



N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

save = dict()
card.sort()
for c in card:
    start = 0
    end = N-1
    if c not in save:
        save[c] = card_count(start, end, card, c)

print(' '.join(str(save[n]) if n in save else '0' for n in check))
