while True:
    num = str(input())
    if num == '0':
        break
    elif num == num[::-1]:
        print('yes')
    elif num != num[::-1]:
        print('no')

