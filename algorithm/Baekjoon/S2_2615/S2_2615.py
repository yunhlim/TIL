input_lst = [0 for i in range(19)]
for i in range(19):
    input_lst[i] = list(map(int, input().split()))
def omok(lst):
    success_cnt = 0 # 여러 번 성공했는지 판단
    success_color = 0   # 이긴 색
    location = []   # 처음 색이 바뀌면 등장
    success_loc = [0,0] # 성공할 때의 위치 기억
    for i in range(19):    # 가로로 오목 체크하는 함수 작성
        black_cnt = 0   # 검은 돌이 연속으로 나오는지 확인
        white_cnt = 0   # 흰 돌이 연속으로 나오는지 확인
        for j in range(19):    #cnt가 5개가 되면 오목 완성
            if black_cnt == 5 or white_cnt == 5:  # 5개가 연속으로 같은 돌이 나오면 다음 돌 확인
                if lst[i][j] != lst[i][j-1]:  # 현재 색과 다음 돌의 색이 다르면 성공
                    success_cnt += 1
                    success_color = lst[i][j-1] # 완성된 색 저장
                    if success_cnt > 1: # 여러 개가 완성되면 0을 출력
                        print(0)
                        return
                    success_loc[:] = location[:]    # 성공한 위치를 저장
            if lst[i][j] == 0:  # 현재 위치에 0이 있으면 cnt 초기화
                black_cnt = 0
                white_cnt = 0
            elif lst[i][j] == 1: # 현재 위치에 검은돌인 1이 있으면 black_cnt 증가
                if black_cnt == 0:  # 처음 검은돌이 나오면 index 저장
                    location = [i, j]
                black_cnt += 1
                if black_cnt == 5 and j == 18: # 마지막 줄에 5개 째 돌이 놓이면 성공
                    success_cnt += 1
                    success_color = 1 
                    if success_cnt > 1: # 여러 개가 완성되면 0을 출력
                        print(0)
                        return
                    success_loc[:] = location[:]    # 성공한 위치를 저장
                white_cnt = 0
            else:   # 현재 위치에 흰돌인 2가 있으면 white_cnt 증가
                if white_cnt == 0:  # 처음 흰 돌이 나오면 index 저장
                    location = [i, j]
                white_cnt += 1
                if white_cnt == 5 and j == 18:
                    success_cnt += 1
                    success_color = 2
                    if success_cnt > 1: # 여러 개가 완성되면 0을 출력
                        print(0)
                        return
                    success_loc[:] = location[:]    # 성공한 위치를 저장
                black_cnt = 0

    for j in range(19):    # 세로로 오목 체크하는 함수 작성
        black_cnt = 0   # 검은 돌이 연속으로 나오는지 확인
        white_cnt = 0   # 흰 돌이 연속으로 나오는지 확인
        for i in range(19):
            if black_cnt == 5 or white_cnt == 5:  
                if lst[i][j] != lst[i-1][j]:  
                    success_cnt += 1
                    success_color = lst[i-1][j]
                    if success_cnt > 1:
                        print(0)
                        return
                    success_loc[:] = location[:]    
            if lst[i][j] == 0:  
                black_cnt = 0
                white_cnt = 0
            elif lst[i][j] == 1: 
                if black_cnt == 0:  
                    location = [i, j]
                black_cnt += 1
                if black_cnt == 5 and i == 18:
                    success_cnt += 1
                    success_color = 1 
                    if success_cnt > 1: # 여러 개가 완성되면 0을 출력
                        print(0)
                        return
                    success_loc[:] = location[:]    # 성공한 위치를 저장
                white_cnt = 0
            else:   
                if white_cnt == 0:  
                    location = [i, j]
                white_cnt += 1
                if white_cnt == 5 and i == 18:
                    success_cnt += 1
                    success_color = 2
                    if success_cnt > 1: # 여러 개가 완성되면 0을 출력
                        print(0)
                        return
                    success_loc[:] = location[:]    # 성공한 위치를 저장
                black_cnt = 0

    # black_cnt = 0
    # white_cnt = 0
    # for i in range(19):    # 대각선 왼쪽 위에서 오른쪽 아래로 내려가는 함수
    #     for j in range(0,19-i):    
    #         if black_cnt == 5 or white_cnt == 5:  
    #             if lst[i][i+j] != lst[i-1][i+j-1]: 
    #                 success_cnt += 1
    #                 success_color = lst[i-1][i+j-1]
    #                 if success_cnt > 1:
    #                     print(0)
    #                     return    
    #                 success_loc[:] = location[:]   
    #         if lst[i][i+j] == 0:  
    #             black_cnt = 0
    #             white_cnt = 0
    #         elif lst[i][i+j] == 1: 
    #             if black_cnt == 0:  
    #                 location = [i, i+j]
    #             black_cnt += 1
    #             whilte_cnt = 0
    #         else:   
    #             if white_cnt == 0:  
    #                 location = [i, i+j]
    #             whilte_cnt += 1
    #             black_cnt = 0

    # black_cnt = 0
    # white_cnt = 0
    # for j in range(j,18): # 대각선 왼쪽 밑에서 오른쪽 위로 올라가는 함수
    #     for i in range(18,j-1,-1):    
    #         if black_cnt == 5 or white_cnt == 5:  
    #             if lst[i][i+j] != lst[i+j-1][i+j-1]: 
    #                 success_cnt += 1
    #                 success_color = lst[i+j-1][i+j-1]
    #                 if success_cnt > 1:
    #                     print(0)
    #                     return     
    #                 success_loc[:] = location[:]   
    #         if lst[i+j][i+j] == 0:  
    #             black_cnt = 0
    #             white_cnt = 0
    #         elif lst[i+j][i+j] == 1: 
    #             if black_cnt == 0:  
    #                 location = [i+j, i+j]
    #             black_cnt += 1
    #             whilte_cnt = 0
    #         else:   
    #             if white_cnt == 0:  
    #                 location = [i+j, i+j]
    #             whilte_cnt += 1
    #             black_cnt = 0
    
    if success_cnt == 1:
        print(success_color)
        print(*success_loc)
    else: print(0)

omok(input_lst)