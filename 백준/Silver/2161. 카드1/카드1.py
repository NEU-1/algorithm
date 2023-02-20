from collections import deque

card = deque(list(range(1, int(input())+1)))
save = []

while card:
    save.append(card.popleft())
    if len(card) == 0:
        break
    card.append(card.popleft())
print(*save)

