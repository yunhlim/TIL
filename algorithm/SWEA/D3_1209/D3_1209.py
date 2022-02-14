for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    for i in range(100):
        row_sum = 0 # 가로방향 합 초기화
        col_sum = 0 # 세로방향 합 초기화
        right_down_sum = 0    # 왼쪽 위에서 오른쪽 아래 대각선 방향 합 초기화
        right_up_sum = 0    # 왼쪽 아래에서 오른쪽 위 대각선 방향 합 초기화
        for j in range(100):
            row_sum += arr[i][j]    # 가로방향 합
            col_sum += arr[j][i]    # 세로방향 합
        right_down_sum += arr[i][i]
        right_up_sum += arr[100-i-1][i]
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
    if max_sum < right_down_sum:
        max_sum = right_down_sum
    if max_sum < right_up_sum:
        max_sum = right_up_sum
    print(f'#{tc} {max_sum}')