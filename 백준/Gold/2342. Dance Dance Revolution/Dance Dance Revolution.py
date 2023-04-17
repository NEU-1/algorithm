import sys
sys.setrecursionlimit(10 ** 6)

def energy_cost(src, dest):
    if src == dest:
        return 1
    elif src == 0:
        return 2
    else:
        return 4 if (src - dest) % 2 == 0 else 3

def dp(pos, left, right):
    if pos == len(sequence):
        return 0
    if memo[pos][left][right] != -1:
        return memo[pos][left][right]

    next_step = sequence[pos]
    left_cost = energy_cost(left, next_step) + dp(pos + 1, next_step, right)
    right_cost = energy_cost(right, next_step) + dp(pos + 1, left, next_step)

    memo[pos][left][right] = min(left_cost, right_cost)
    return memo[pos][left][right]

sequence = list(map(int, sys.stdin.readline().split()))
sequence.pop()

memo = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(len(sequence))]
print(dp(0, 0, 0))
