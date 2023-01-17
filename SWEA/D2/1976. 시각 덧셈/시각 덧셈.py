T = int(input())
for t in range(1, T+1):
        
    time = list(map(int,input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]

    if minute > 60:
        hour += (minute//60)
        minute %= 60

    if hour > 12:
        hour %= 12
        if hour == 0:
            hour += 12

    print(f'#{t} {hour} {minute}')