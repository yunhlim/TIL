def recur(cur, prv_d):
    global cnt, balls
    if cnt <= cur:      # 이미 나온 결과보다 더 횟수가 많거나 같으면 종료
        return
    if cur == 10:       # 10번 넘게 움직였으면 종료
        return

    balls_origin = [balls[0][:], balls[1][:]]       # 공의 위치를 기억
    for d in range(4):
        balls = [balls_origin[0][:], balls_origin[1][:]]    # 공의 위치를 움직였으니 원상복구
        if prv_d >= 0 and (d % 2 == prv_d % 2):   # 같은 방향이거나 반대 방향인 경우는 보지 않는다.
            continue                            # 처음에만 방향을 -1로 설정해 모든 방향을 확인하도록 한다.
        if red_order(d):
            if move(0, d):  # 빨간 공이 빠지는 경우
                if move(1, d):  # 파란 공이 빠지는 경우
                    continue
                cnt = min(cur + 1, cnt)
                return
            if move(1, d):  # 파란 공이 빠지는 경우
                continue
        else:
            if move(1, d):  # 파란 공이 빠지는 경우
                continue
            if move(0, d):  # 빨간 공이 빠지는 경우
                cnt = min(cur + 1, cnt)
                return
        recur(cur + 1, d)
    

def red_order(dir):
    red_order = balls[0][0] * dx[dir] + balls[0][1] * dy[dir]
    blue_order = balls[1][0] * dx[dir] + balls[1][1] * dy[dir]
    if red_order >= blue_order:  # 빨간 공이 움직이는 방향의 벽에 더 가까이 있는 경우
        return 1
    else:
        return 0


def move(color, dir):    # 공 움직이기
    x, y = balls[color]     # 고른 공의 좌표
    x_another, y_another = balls[1^color] # 다른 색 공의 좌표
    while True:
        x += dx[dir]
        y += dy[dir]
        if arr[x][y] == '#' or (x == x_another and y == y_another):      # 벽을 만나는 경우 or 다른 색 공을 만난 경우
            balls[color][0] = x - dx[dir]
            balls[color][1] = y - dy[dir]
            return 0
        elif arr[x][y] == 'O':    # 골인 되는 경우
            balls[color][0] = -1
            balls[color][1] = -1
            return 1

dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
balls = [[], []]    # red, blue 공
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            balls[0] = [i, j]
            arr[i][j] = '.'
        if arr[i][j] == 'B':
            balls[1] = [i, j]
            arr[i][j] = '.'

cnt = 11
recur(0, -1)

if cnt == 11:
    print(-1)
else:
    print(cnt)