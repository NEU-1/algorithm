num, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort
save = 0

for c1 in range(num-2):
    for c2 in range(c1+1, num-1):
        for c3 in range(c2+1, num):
            if card[c1] + card[c2] + card[c3] == M:
                save = M
            elif save < card[c1] + card[c2] + card[c3] < M:
                save = card[c1] + card[c2] + card[c3]

print(save)
