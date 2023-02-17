for t in range(1, 11):
    num = int(input())
    word = list(input())
    stack = []
    out = []
    for w in word:
        if w == '+':
            if len (stack) != 0 and stack[-1] == '+':
                out.append(stack.pop())
            stack.append(w)
        else:
            out.append(w)
    while stack:
        out.append(stack.pop())
    # print(out)

    for o in out:
        if o.isnumeric():
            stack.append(int(o))
        else:
            a = stack.pop()
            b = stack.pop()
            if o == '+':
                stack.append(a+b)
    print(f'#{t} {stack[0]}')
