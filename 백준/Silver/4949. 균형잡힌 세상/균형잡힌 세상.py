while True:
    save = []
    word = input()
    if word == '.':
        break
    elif word.count('(') != word.count(')') or word.count('[') != word.count(']'):
        print('no')
    else:
        for w in word:
            if w == '(' or w == '[':
                save.append(w)
            elif w == ')':
                if len(save) > 0 and save[-1] == '(':
                    save.pop(-1)
                else:
                    print('no')
                    break
            elif w == ']':
                if len(save) > 0 and save[-1] == '[':
                    save.pop(-1)
                else:
                    print('no')
                    break
        else:
            print('yes')
