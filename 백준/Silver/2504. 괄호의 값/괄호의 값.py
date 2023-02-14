import sys
input = sys.stdin.readline

s = list(input().rstrip())[::-1]

def cal(start):
    r = 0
    while s:
        a = s.pop()
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1,r)
        elif start == "[" and a == "]":
            return 3 * max(1,r)
    
    print(0)
    sys.exit()

ans = 0    
while s:
    ans += cal(s.pop())
print(ans)