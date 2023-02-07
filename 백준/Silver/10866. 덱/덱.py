import sys

N = int(sys.stdin.readline())
deque = []
for n in range(N):
    word = sys.stdin.readline().split()
    order = word[0]
    if order == 'push_front':
        deque.insert(0, word[1])
    elif order == 'push_back':
        deque.append(word[1])
    elif order == 'pop_front':
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif order == 'pop_back':
        if len(deque) > 0:
            print(deque.pop(-1))
        else:
            print(-1)
    elif order == 'size':
        print(len(deque))
    elif order == 'empty':
        if len(deque) > 0:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    elif order == 'back':
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)
