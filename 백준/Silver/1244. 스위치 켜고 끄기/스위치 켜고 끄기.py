def TF(num):
    return 0 if num == 1 else 1

def man(num):
    for m in range(num-1, switch_num, num):
        light[m] = TF(light[m])
    return light

def woman(num):
    light[num-1] = TF(light[num-1])
    i = 1
    while num + i -1 < switch_num and num-i-1 >= 0 and light[num-i-1] == light[num+i-1]:
        light[num-i-1] = TF(light[num-i-1])
        light[num+i-1] = TF(light[num+i-1])
        i += 1
    return light


switch_num = int(input())
light = list(map(int,input().split()))
human = int(input())
for z in range(human):
    s, num = map(int, input().split())
    light = man(num) if s == 1 else woman(num)

if len(light) > 20:
    for z in range(0,len(light),20):
        print(*light[z:z+20]) # 언패킹 + 20개 컷
else:
    print(*light)