import sys

s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []

for c in s:
    stack.append(c)
    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
