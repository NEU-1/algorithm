T = int(input()) # 테스트 횟수
save_list = [1] # 결과물 저장소
# num_save_list 결과물 길이
list_1 = [1] # 앞쪽 계산
list_2 = [1] # 뒤쪽 계산
w_count = 0 # 파스칼 높이 체크
# l 테스트 횟수 for 
# i 파스칼 높이 for

for l in range(1, T+1):
    N = int(input()) # 파스칼 높이
    print(f'#{l}')
    print(1)
    if N>1:
        while w_count < N-1:
            num_save_list = len(save_list)
            save_list = []
            save_list.append(list_1[0])
            if num_save_list > 1:
                for i in range(1, num_save_list):
                    save_list.append(list_1[i] + list_2[i-1])
            save_list.append(list_2[num_save_list-1])
            list_1 = save_list
            list_2 = save_list
            print(*save_list)
            w_count += 1
    w_count = 0
    list_1 = [1] # 앞쪽 계산
    list_2 = [1] # 뒤쪽 계산
    save_list = [1] # 결과물 저장소

