save = []
for four in range(4):
    x, y, x1, y1 = map(int,input().split())
    for Y in range(y,y1):
        for X in range(x,x1):
            save.append(str(X)+str(Y))
# print(save)
save = set(save)
# print(save)
print(len(save))

