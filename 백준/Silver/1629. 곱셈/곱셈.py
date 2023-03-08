import sys
sys.setrecursionlimit(10**6)

A, B, C = map(int,input().split())

def x(A,B,C):
    if B == 1:
        return A%C
    
    nxt = x(A,B//2,C)

    if B%2==0:
        return nxt**2%C
    else:
        return nxt**2*A%C
    

print(x(A,B,C))


