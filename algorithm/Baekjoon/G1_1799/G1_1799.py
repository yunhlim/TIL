def in_range(x, y):     # 체스판 위에 있는지 체크
    return 0 <= x < n and 0 <= y < n


def check(x, y):        # 현재 위치의 대각선으로 비숍이 놓여 있는지 확인
                        # 비숍을 위에서 아래로 놓으니 위쪽만 확인한다.
    # 오른쪽 위 체크
    nx = x + dx[0]
    ny = y + dy[0]
    while in_range(nx, ny):
        if visited[nx][ny]:
            return False        # 비숍이 대각선 방향에 놓여있다.
        nx += dx[0]
        ny += dy[0]
    # 왼쪽 위 체크
    nx = x + dx[1]
    ny = y + dy[1]
    while in_range(nx, ny):
        if visited[nx][ny]:
            return False        # 비숍이 대각선 방향에 놓여있다.
        nx += dx[1]
        ny += dy[1]
    
    return True     # 대각선 방향에 비숍이 없다.


def recur(cur, cnt):
    global max_cnt
    if cur == place_cnt:        # 놓을 수 있는 자리를 다 확인한 경우
        max_cnt = max(max_cnt, cnt)
        return
    # 가지치기
    if place_cnt - cur + cnt <= max_cnt:     # 앞으로 비숍으로 다 채워도 현재 구한 최대값보다 작거나 같은 경우
        return

    x, y = is_place[cur]
    if check(x, y):                     # 비숍을 놓을 수 있는지 확인
        visited[x][y] = 1
        recur(cur + 1, cnt + 1)        # 비숍을 놓는 경우
        visited[x][y] = 0
    
    recur(cur + 1, cnt)    # 비숍을 놓지 않는 경우
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
is_place = []       # 비숍을 놓을 수 있는 자리
for i in range(n):  # 비숍을 놓을 수 있는 자리를 왼쪽 위부터 순차적으로 리스트에 담는다.
    for j in range(n):
        if arr[i][j]:
            is_place.append([i, j])
place_cnt = len(is_place)
visited = [[0] * n for _ in range(n)]
dx = [-1, -1] # 오른쪽 위, 왼쪽 위 순서
dy = [1, -1]
max_cnt = 0
recur(0, 0)
print(max_cnt)