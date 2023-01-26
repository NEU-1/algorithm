num = int(input())
num_dict = dict()
for n in range(num):
    word = input()
    num_dict[word]=len(word)

sorted_num=sorted(num_dict.items(), key = lambda x: (x[1], x[0]))
for i in list(dict(sorted_num).keys()):
    print(i)




''' 
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''