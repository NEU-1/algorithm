T = int(input())
for t in range(T):
    word = list(input())
    num_max = int(input())
    case = input()[1:-1].split(',')
    r = 1
    num_min = 0
    # case = map(int, case)
    # print(type(case))
    if word.count('D') > num_max:
        print('error')
        continue
    else:
        for w in word:
            if w == 'R':
                r *= -1
            elif w == 'D':
                if r == 1:
                    num_min += r
                else:
                    num_max += r
        case = case[num_min:num_max]
        case = case[::r]

        if num_max == 0:
            print(case)
        else:
            print('[',end='')
            print(",".join(case), end='')
            print(']')

