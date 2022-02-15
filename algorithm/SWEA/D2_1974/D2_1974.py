T = int(input())
for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)] # 입력받은 스도쿠 퍼즐
    result = 1  # 중간에 문제 
    for i in range(9):  # row, column 탐색
        row_set = set() # row의 숫자를 담을 set
        col_set = set() # column의 숫자를 담을 set
        for j in range(9):  # 숫자를 담는다.
            row_set = row_set | {arr[i][j]} 
            col_set = col_set | {arr[j][i]}
        if len(row_set) != 9 or len(col_set) != 9:  # 1~9중 하나라도 중복되면 길이가 9가 나오지 않음을 이용
            result = 0
            break
    if result:  # 위에서 만족시키지 못한 경우가 나오면 네모 탐색을 하지 않는다.
        for i in range(3):  #3X3 네모 탐색
            for j in range(3):
                num_set = set()
                for k in range(3*i, 3*i+3): # 네모의 맨 왼쪽 위 인덱스부터 3x3 네모모양을 탐색
                    for l in range(3*j, 3*j+3):
                        num_set = num_set | {arr[k][l]}
                if len(num_set) != 9:
                    result = 0
                    break
    print(f'#{tc} {result}')