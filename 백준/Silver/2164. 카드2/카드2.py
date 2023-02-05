# card = list(range(1, int(input())+1))
# for c in range(100):
#     card = list(range(1, c+2))
#     while len(card)>1:
#         del card[0]
#         if len(card) == 1:
#             break
#         card.append(card.pop(0))

#     print(card)

card = int(input())
if card == 1:
    print(1)
else:
    num = 1
    while card > num:
        num *= 2

    end = 2*card - num
    print(end)