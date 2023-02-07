import sys

N = int(sys.stdin.readline())
que = []
for n in range(N):
    word = sys.stdin.readline().split()
    order = word[0]
    if order == 'push':
        que.append(word[1])
    elif order == 'pop':
        if len(que) > 0:
            print(que.pop(0))
        else:
            print(-1)
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if len(que) > 0:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    else:
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)