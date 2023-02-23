a, b = map(int,input().split())

left = 0
right = 0

while a >1 or b > 1:
    if a > b:
        a -= b
        left += 1
    else:
        b -= a
        right += 1

print(left, right)