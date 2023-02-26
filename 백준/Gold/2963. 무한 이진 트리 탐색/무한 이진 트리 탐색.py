word = input()

now = 1
star = 1
for w in word:
    if w == 'L':
        now*=2
    elif w == 'R':
        now = now*2 + star
    elif w == '*':
        now = now*5 + star
        star *= 3

print(now)