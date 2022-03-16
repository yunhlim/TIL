from collections import deque


t = int(input())
for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())   # 전체 크기: n x m, 맨홀: (r, c), 소요 시간: l
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 터널의 모양이 1~7이므로 길이 8인 배열 선언, 각각 우 하 좌 상으로 연결되는지 표시
    tunnel_arr = [0, [1, 1, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
    dy = [0, 1, 0, -1]  # 우 하 좌 상
    dx = [1, 0, -1, 0]
    queue = deque()
    cnt = 0     # 탈주범이 있는 터널의 개수
    queue.append((r, c, 1))    # 맨홀과 시작점의 터널 개수


    while queue:
        y, x, time = queue.popleft()
        if arr[y][x] == 0:  # 확인한 값이면 break
            continue
        cnt += 1        # 새로운 터널이니 1 추가

        tunnel = tunnel_arr[arr[y][x]]  # 현재 터널의 모양
        arr[y][x] = 0       # 확인한 위치는 다시 보지 않기 위해 0으로 바꾼다.

        if time == l:       # 더 이상 진행할 수 없는 시간이니 continue
            continue
        
        for i in range(4):  # 우 하 좌 상 네 방향 확인
            if tunnel[i]:   # 터널이 그쪽 방향으로 뚫려있는지 확인
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 0:    # 이동 방향이 배열을 초과하지 않고, 터널이 있는지
                    # 이동 방향에 반대 방향으로 터널이 뚫려 있는지 ex). 오른쪽에는 왼쪽이, 아래에는 위쪽이 뚫려야 함.
                    if tunnel_arr[arr[ny][nx]][(i + 2) % 4]:
                        queue.append((ny, nx, time + 1))    # 뚫려있으면 큐에 넣는다.
    print(f'#{tc} {cnt}')