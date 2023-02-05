def bhh(num):
    num += sum(map(int,(list(str(num)))))
    return(num)

# print(bhh(5485))

number = int(input())
check = number - int(list(str(number))[0]) - (len(list(str(number)))-1)*9
while check < number:
    if bhh(check) == number:
        print(check)
        break
    else:
        check += 1
else:
    print(0)
# print('spam ' 'eggs' or 'spam eggs')	
# print('spam ' 'eggs'    '\r''eggs spam')