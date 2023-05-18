import math

n = 0
max_cost = 0
cost = [[0 for _ in range(16)] for _ in range(16)]
dp = [[[0 for _ in range(10)] for _ in range(16)] for _ in range(1<<16)]
answer = 1

def get_answer(state):
    div = 2 ** 15
    ret = 0

    while div > 0:
        if state >= div:
            state -= div
            ret += 1
        div //= 2

    return ret

def set_dp():
    global answer
    dp[1][1][0] = 1

    for i in range(1, 1 << n):
        state = i

        for j in range(n):
            for c in range(max_cost + 1):
                if dp[i][j + 1][c] == 0:
                    continue
                answer = max(answer, get_answer(i))

                if state & (1 << j):
                    for k in range(n):
                        if state & (1 << k):
                            continue
                        newstate = state | (1 << k)
                        if cost[j + 1][k + 1] < c:
                            continue
                        dp[newstate][k + 1][cost[j + 1][k + 1]] = 1

def init():
    global n, max_cost
    n = int(input())
    
    for i in range(1, n + 1):
        input_string = input()
        for j in range(1, n + 1):
            cost[i][j] = int(input_string[j - 1])
            max_cost = max(max_cost, cost[i][j])

def main():
    init()
    set_dp()
    print(answer)

if __name__ == "__main__":
    main()
