import sys

def reverse_word(word):
    return word[::-1]

word = sys.stdin.readline().strip()
stack = []
result = ""

check = False
for w in word:
    if w == "<":
        result += reverse_word("".join(stack))
        result += "<"
        stack = []
        check = True
    elif w == ">":
        result += ">"
        check = False
    elif check:
        result += w
    elif w == " ":
        result += reverse_word("".join(stack))
        stack = []
        result += " "
    else:
        stack.append(w)

result += reverse_word("".join(stack))

print(result)
