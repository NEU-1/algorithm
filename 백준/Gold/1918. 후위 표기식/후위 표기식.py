import sys

def change(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '(':
        return 0

word = sys.stdin.readline().rstrip()  
stack = [] 
result = ''  

for w in word:
    if w.isalpha():  
        result += w
    elif w == '(': 
        stack.append(w)
    elif w == ')':  
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()  
    else: 
        while stack and change(stack[-1]) >= change(w):
            result += stack.pop()
        stack.append(w)

while stack:  
    result += stack.pop()

print(result)
