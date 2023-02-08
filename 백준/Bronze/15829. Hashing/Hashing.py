_ = input()
word = list(input())
save = 0
for w in range(len(word)):
    save += (ord(word[w])-96)*(31**w)
print(save)