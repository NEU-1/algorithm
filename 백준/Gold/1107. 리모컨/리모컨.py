def check(num, broken):
    # 고장난 버튼이 포함되어 있는지 확인하는 함수
    for N in str(num):
        if N in broken:
            return False
    return True

def move(num, broken):
    # 주어진 번호로 이동하기 위한 최소 버튼 조작 횟수를 구하는 함수
    if num == 100: # 100번 채널에서 시작하는 경우
        return 0
    mn_cnt = abs(num - 100) # + 또는 - 버튼만을 사용하는 경우
    for i in range(1000001):
        if check(i, broken):
            cnt = abs(num - i) + len(str(i))
            if cnt < mn_cnt:
                mn_cnt = cnt
    return mn_cnt

N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼의 개수
if M == 0: # 고장난 버튼이 없는 경우
    print(min(len(str(N)), abs(N - 100)))
else:
    broken = list(input().split()) # 고장난 버튼
    if len(broken) == 10:
        print(abs(N-100))
    else:
        for i in range(1000001):
            if check(i, broken):
                print(min(len(str(i)) + abs(i - N), move(N, broken)))
                break
