sam = [0] * 101
sam[1] = 1
sam[2] = 1
sam[3] = 1
sam[4] = 2
sam[5] = 2
for s in range(5,101):
    sam[s] = sam[s-1] + sam[s-5]
for _ in range(int(input())):
    print(sam[int(input())])