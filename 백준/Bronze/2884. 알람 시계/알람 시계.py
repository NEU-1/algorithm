hour, minute = list(map(int, input().split()))

if minute < 45:
    hour -= 1
    minute += 60
    if hour == -1:
        hour += 24
print(f'{hour} {minute-45}')