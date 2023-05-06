import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

def coun(x):
    if x <= 0:
        return 0

    inp = int(math.log2(x))  
    two = 2 ** inp  
    if two == x:
        return inp * x // 2 + 1

    diff = x - two
    return coun(two) + diff + coun(diff)

a, b = map(int, input().split())
print(coun(b) - coun(a - 1))
