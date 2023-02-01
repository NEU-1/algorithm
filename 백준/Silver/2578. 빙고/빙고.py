num = [list(map(int,input().split())) for _ in range(10)]
qube = num[:5]
answer = num[5:]
# print(qube, answer)
count = 0
count_bingo = 0
for y in range(5):
    for x in range(5):
        # answer 출력용
        for qube_y in range(5):
            for qube_x in range(5):
                # qube 탐색용
                if answer[y][x] == qube[qube_y][qube_x]:
                    qube[qube_y][qube_x] = 0
                    count += 1
        # if count == 15:
        #     print(qube)
        # print(qube)
        save1 = []
        save2 = []
        save3 = []
        save4 = []
        count_bingo = 0
        for Y in range(5):
            for X in range(5):
                save1.append(qube[Y][X])
                save2.append(qube[X][Y])
            save3.append(qube[Y][Y])
            save4.append(qube[4-Y][Y])
                # print(save3)
                

            if save1 == [0,0,0,0,0]:
                count_bingo += 1
                # print(count_bingo)
                # print(save1)
            if save2 == [0,0,0,0,0]:
                count_bingo += 1
                # print(count_bingo)
                # print(save2)
            if save3 == [0,0,0,0,0]:
                count_bingo += 1
                # print(count_bingo)
                # print(save3)
            if save4 == [0,0,0,0,0]:
                count_bingo += 1
                # print(count_bingo)
                # print(save4)
            # print(qube)
            # print(count_bingo)
        
            save1 = []
            save2 = []
        if count_bingo >= 3:
            print(count)
            exit()