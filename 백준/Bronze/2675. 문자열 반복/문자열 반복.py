run = int(input())
for r in range(run):
    count, word = list(input().split())
    save = []
    for w in word:
        save+=w*int(count)
    print(''.join(save))