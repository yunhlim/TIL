input_lst = [0 for i in range(19)]
for i in range(19):
    input_lst[i] = list(map(int, input().split()))

def omok(lst):
    win = 0 # 0이면 승부x, 1이면 검은돌 승리, 2이면 흰돌 승리
    position = 0
    for i in range(19): # 이중 for 문으로 오목이 완성될 수 있는 시작점을 하나씩 선택
        for j in range(15): # 시작점에서 오른쪽으로 오목이 완성되는지 확인
            if lst[i][j] != 0:  # 바둑돌이 놓여 있을 때
                if j == 0 or lst[i][j] != lst[i][j-1]:  
                    # 바둑돌 왼쪽에 값이 없거나, 있을 때는 색이 다르면 시작점으로 선택한다.
                    for k in range(1,5): # 5개가 나란히 있는지 확인
                        if lst[i][j] != lst[i][j+k]:
                            break
                    else:
                        if j == 14 or lst[i][j] != lst[i][j+5]: # 오른쪽으로 더 놓을 자리가 없거나 오른쪽에 놓인 것이 다른 색인지 확인.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(15): # 이중 for 문으로 오목이 완성될 수 있는 시작점을 하나씩 선택
        for j in range(19): # 시작점에서 아래쪽으로 오목이 완성되는지 확인
            if lst[i][j] != 0:  # 바둑돌이 놓여 있을 때
                if i == 0 or lst[i][j] != lst[i-1][j]:
                    # 바둑돌 위쪽에 값이 없거나, 있을 때는 색이 다르면 시작점으로 선택한다.
                    for k in range(1,5): # 5개가 나란히 있는지 확인
                        if lst[i][j] != lst[i+k][j]:
                            break
                    else:
                        if i == 14 or lst[i][j] != lst[i+5][j]: # 아래쪽으로 더 놓을 자리가 없거나 아래쪽에 놓인 것이 다른 색인지 확인.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(15): # 이중 for 문으로 오목이 완성될 수 있는 시작점을 하나씩 선택
        for j in range(15):    # 시작점에서 오른아래쪽으로 오목이 완성되는지 확인
            if lst[i][j] != 0:  # 바둑돌이 놓여 있을 때              
                if i == 0 or j == 0 or lst[i][j] != lst[i-1][j-1]: 
                    # 바둑돌 왼쪽이나 위쪽에 값이 없거나, 있을 때는 색이 다르면 시작점으로 선택한다.
                    for k in range(1,5): # 5개가 나란히 있는지 확인
                        if lst[i][j] != lst[i+k][j+k]:
                            break
                    else:
                        if i == 14 or j == 14 or lst[i][j] != lst[i+5][j+5]: # 오른쪽, 아래쪽으로 더 놓을 자리가 없거나 오른아래쪽에 놓인 것이 다른 색인지 확인.
                            win = lst[i][j]
                            position = (i+1,j+1)

    for i in range(18,3,-1): # 이중 for 문으로 오목이 완성될 수 있는 시작점을 하나씩 선택
        for j in range(15): # 시작점에서 오른위쪽으로 오목이 완성되는지 확인
            if lst[i][j] != 0:  # 바둑돌이 놓여 있을 때
                 if i == 18 or j == 0 or lst[i][j] != lst[i+1][j-1]:
                    # 바둑돌 왼쪽이나 아래쪽에 값이 없거나, 있을 때는 색이 다르면 시작점으로 선택한다.
                    for k in range(1,5): # 5개가 나란히 있는지 확인
                        if lst[i][j] != lst[i-k][j+k]:
                            break
                    else:
                        if i == 4 or j == 14 or lst[i][j] != lst[i-5][j+5]: # 오른쪽, 위쪽으로 더 놓을 자리가 없거나 오른위쪽에 놓인 것이 다른 색인지 확인.
                            win = lst[i][j]
                            position = (i+1,j+1)
    if win == 0:    # 승부가 나지 않으면 0만 출력
        print(win)
        return
    print(win)  # 승부가 났으니 승리한 돌을 출력한 후 위치를 출력한다.
    print(*position)

omok(input_lst)