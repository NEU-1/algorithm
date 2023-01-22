word = list(input())
# print(word)
len_word = len(word)
dict_word = dict()
# print(a_z)
for j in range(97, 123):
    dict_word.setdefault(chr(j),-1)
# print(dict_word)
for i in range(len_word):
    if word[i] in dict_word and dict_word[word[i]] == -1:
        dict_word[word[i]] = i
print(*dict_word.values())