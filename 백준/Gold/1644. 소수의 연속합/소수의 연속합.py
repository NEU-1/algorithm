# 입력된 값을 에라토네스로 돌려서 소수만 추출

# 리스트 뒤에부터 더해가면서
# 입력값 초과시 시작 포인트 이동

# 엔드값은 다 더해도 입력값 안되는곳

def make_prime(num): # 소수 판별
    check = [0]*(num+1)
    prime = []
    for i in range(2, int(num**0.5)+1):
        if check[i] == 0:
            for j in range(i*2, num+1, i):
                check[j] = 1
    for k in range(2, num+1):
        if check[k] == 0:
            prime.append(k)
    return prime

def find_end(prime, num): # 끝값 탐색
    save = 0
    for p in range(len(prime)):
        save += prime[p]
        if save >= num:
            return p

def 소수합(prime, p, num):
    count = 0
    if num <= 1:
        return 0
    for z in range(len(prime)-1, p-1, -1):
        count = hap(prime, z, num, count)   
    return count

def hap(prime, z, num, count):
    cut = 0
    for i in range(z, -1, -1):
        cut += prime[i]
        if cut == num:
            count += 1
            return count
        elif cut > num:
            return count

num = int(input())
prime = make_prime(num)
p = find_end(prime, num)
# print(prime,p)
count = 소수합(prime, p, num)

print(count)
