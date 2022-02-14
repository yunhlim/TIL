T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # N x N 배열
    ni, nj, di, dj = 0, 0, 0, 1   # 현재 위치(0, 0)와 움직이는 방향(우)

    arr[0][0] = 1
    for i in range(2, N * N + 1):
        if dj == 1:
            if nj == N-1 or arr[ni][nj+1] != 0:  # 오른쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 1, 0   # 아래쪽으로 경로 변경
        if dj == -1:
            if nj == 0 or arr[ni][nj-1] != 0:  # 왼쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = -1, 0   # 위쪽으로 경로 변경
        if di == 1:
            if ni == N-1 or arr[ni+1][nj] != 0:  # 아래쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 0, -1   # 왼쪽으로 경로 변경
        if di == -1:
            if ni == 0 or arr[ni-1][nj] != 0:  # 위쪽으로 움직일 곳이 없거나 이미 채워진 자리인 경우
                di, dj = 0, 1   # 오른쪽으로 경로 변경
        ni += di
        nj += dj
        arr[ni][nj] = i  # 현재 위치에 정수를 적는다.
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])