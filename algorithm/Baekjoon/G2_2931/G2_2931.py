def pipe(x, y, dir):
    if arr[x][y] == 'Z':    # Z가 나오면 다 방문했는지 표시
        return True
    if arr[x][y] == '.':    # .인 경우는 False
        return False

    block = arr[x][y]       # 현재 블록 값을 적어준다.
    # 시작할 때, 네 방향을 확인한다.
    if dir == -1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and arr[nx][ny] != '.' and (i + 2) % 4 in blocks[arr[nx][ny]]:
                return pipe(nx, ny, i)
    elif (dir + 2) % 4 in blocks[block]:
        # '|-+' 블록인 경우
        if block in '|-+':
            nx = x + dx[dir]
            ny = y + dy[dir]
            if in_range(nx, ny):
                return pipe(nx, ny, dir)

        else:                               # 꺾이는 블록인 경우
            for nxt_d in blocks[block]:         # 순회하면 방향은 2가지
                if nxt_d != (dir + 2) % 4:      # 진행방향과 다른 방향으로 이동
                    nx = x + dx[nxt_d]
                    ny = y + dy[nxt_d]
                    if in_range(nx, ny):
                        return pipe(nx, ny, nxt_d)
    return False


def in_range(x, y):     # 배열을 넘어가는지 확인
    return 0 <= x < r and 0 <= y < c


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
# block은 +보다 |와 -를 먼저보도록 설계해야 한다.
# 우 하 좌 상 0, 1, 2, 3
blocks = {'|': [1, 3], '-': [0, 2], '+': [0, 1, 2, 3],
          '1': [0, 1], '2': [0, 3], '3': [2, 3], '4': [1, 2]}
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# 자그레브와 모스코바 위치 찾기
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'M':
            m = (i, j)

# 완탐: 각 . 지점에 모든 블록을 넣어준다.
for i in range(r):
    for j in range(c):
        if arr[i][j] == '.':
            for block in blocks:        # 7가지 블록을 넣어가며 확인
                visited = [[0] * c for _ in range(r)]   # 다 방문했는지 확인
                arr[i][j] = block       # 블록을 바꿔준다.
                if pipe(*m, -1):        # 완성한 경우
                    print(i + 1, j + 1, block)      # 출력
                    exit()
            arr[i][j] = '.'
