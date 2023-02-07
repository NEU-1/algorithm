import sys

N = int(sys.stdin.readline())
stack = []
for n in range(N):
    word = sys.stdin.readline().split()
    order = word[0]
    if order == 'push':
        stack.append(word[1])
    elif order == 'pop':
        if len(stack) > 0:
            print(stack.pop(-1))
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)