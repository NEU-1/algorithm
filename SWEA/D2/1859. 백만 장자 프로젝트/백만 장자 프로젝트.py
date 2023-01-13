

#케이스 수 입력
T = int(input())

for l in range(1,T+1):
    
    #거래 일 수
    n = int(input())

    #일 별 가격
    cost = list(map(int,input().split()))

    #시작점
    start = cost[n-1]
    
    #차액 저장
    money = 0
    
    #for문 뒤로 돌리기
    for i in range(1, n):
        #뒤로 돌리기 세부
        if start-cost[n-i-1] > 0:
            money += (start-cost[n-i-1])
        elif start-cost[n-i-1] < 0:
            start = cost[n-i-1]
    print(f'#{l} {money}')
        

