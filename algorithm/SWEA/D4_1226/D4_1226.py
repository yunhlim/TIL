def miro():     # 미로 결과 가능 여부 판별
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:  # 시작점 확인
                s = (i, j)
    stack = [s]

    while stack:
        v = stack.pop()
        y, x = v[0], v[1]
        arr[y][x] = 1   # 가지치기를 위해 현재 위치를 벽으로 만든다.
        for i in range(4):      # 네 방향으로 확인
            ny = y + dy[i]
            nx = x + dx[i]
            if arr[ny][nx] == 0:    # 길인지 확인하고 길이면 stack에 담는다.
                stack.append((ny, nx))
            elif arr[ny][nx] == 3:  # 도착점에 도달하는지 확인
                return 1
    return 0        # 도달하지 않는 경우


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dy = [0, 1, 0, -1]  # 우 하 좌 상
    dx = [1, 0, -1, 0]
    
    print(f'#{tc} {miro()}')