import sys

def prime():
    a = (2*(10**6))+1
    check = [0] * a
    check[0], check[1] = 1, 1
    for i in range(2, int(a**0.5)+1):
        if check[i] == 0:
            for j in range(i*2, a, i):
                check[j] = 1
    return [z for z in range(2, a) if check[z] == 0]

def goldbah(num, prime):
    num_2 = num**2
    for p in prime:
        if p > num_2:
            break
        if num % p == 0 and num != p:
            return 'NO'
    return'YES'
        


T = int(sys.stdin.readline())
save = []
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split())
    save.append(a+b)

prime = prime()

for s in save:
    if s < 4:
        print('NO')
    elif s % 2 == 0:
        print('YES')
    else:
        s -= 2
        print(goldbah(s, prime))

