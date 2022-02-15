T = 10

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    X_lst = []  # 시작점 배열
    min_row_move = 10000    # 가로방향으로 움직이는 횟수를 센다
    min_X = 0   # 최단 경로 X
    for i in range(100):    # 아래 2를 찾고 거기서부터 올라간다!
        if ladder[0][i] == 1:
            X_lst.append(i)

    for X in X_lst:
        dir = (1, 0)  # 처음에는 내려간다.  # 아래쪽 di = 1, dj = 0
        current = (0, X)   # 시작 인덱스
        cnt_row_move = 0 # 가로방향으로 움직이는 횟수
        while current[0] != 99:  # 맨 아래로 내려가면 끝(0번째 인덱스)
            ni, nj = current
            if dir != (1, 0):   # 움직이던 방향이 가로 방향인 경우
                if not(0 <= nj+dir[1] < 100 and ladder[ni][nj+dir[1]]): # 가던 방향으로 움직일 수 있는지 판단
                    dir = (1, 0)   # 못가면 아래로  # 아래쪽 di = 1, dj = 0
            else:           # 움직이던 방향이 아래 방향인 경우
                if 0 <= nj-1 < 100 and ladder[ni][nj-1]:    # 왼쪽으로 움직일 수 있는지 판단
                    dir = (0, -1)   # 왼쪽 di = 0, dj = -1
                if 0 <= nj+1 < 100 and ladder[ni][nj+1]:    # 오른쪽으로 움직일 수 있는지 판단
                    dir = (0, 1)    # 오른쪽 di = 0, dj = 1

            if dir != (1, 0):
                cnt_row_move += 1
            current = (ni+dir[0], nj+dir[1])    # 이동시킨다.

        if min_row_move >= cnt_row_move:    # 가로로 제일 조금 움직이는지 확인
            min_X = X
            min_row_move = cnt_row_move

    print(f'#{tc} {min_X}')