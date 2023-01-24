num1, num2 = list(map(int, input().split()))
sangsu_num1 = int(list(str(num1))[2])*100+int(list(str(num1))[1])*10+int(list(str(num1))[0])
sangsu_num2 = int(list(str(num2))[2])*100+int(list(str(num2))[1])*10+int(list(str(num2))[0])

print(sangsu_num2 if sangsu_num2>sangsu_num1 else sangsu_num1)
