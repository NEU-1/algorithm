# 큐브 생성
Y, X = map(int,input().split())
qube = [list(input())for n in range(Y)]
count_white = 0
count_black = 0
draw = []
# print(qube)
# 체스판 제작
chess_white = []
chess_black = []
for i in range(8):
    if i%2 == 0:
        chess_white.append(list('WBWBWBWB'))
        chess_black.append(list('BWBWBWBW'))
    else:
        chess_white.append(list('BWBWBWBW'))
        chess_black.append(list('WBWBWBWB'))
# print(chess_white, chess_black)
# 각 포인트를 이동
for y in range(Y-7):
    for x in range(X-7):
    # 포인트별 8*8을 탐색
        for y_move in range(8):
            for x_move in range(8):
    # 탐색구간 시작을 w, b 두가지 경우
                # print(chess_white[y_move][x_move])
                if qube[y+y_move][x+x_move] != chess_white[y_move][x_move]:
                    count_white += 1
                if qube[y+y_move][x+x_move] != chess_black[y_move][x_move]:
                    count_black += 1
    # 각 경우별 최소값을 비교
        draw.append(min(count_white, count_black))
        # print(count_white, count_black)
        count_white = 0
        count_black = 0
    # 전체 최소값을 비교
print(min(draw))
draw = []
