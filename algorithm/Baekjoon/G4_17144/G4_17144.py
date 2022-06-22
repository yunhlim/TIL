def in_range(x, y):     # 범위 안에 있는지 확인
    return 0 <= x < r and 0 <= y < c


def spread():       # 미세먼지 확산
    global arr
    copy_arr = [arr[i][:] for i in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] > 0:       # 미세먼지가 있는 경우
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not in_range(nx, ny) or arr[nx][ny] == -1:   # 범위를 벗어나거나 공기청정기인 경우
                        continue
                    copy_arr[nx][ny] += arr[x][y] // 5      # 방향으로 확산
                    copy_arr[x][y] -= arr[x][y] // 5        # 확산한 만큼 가운데 부분의 값을 빼준다.
    arr = [copy_arr[i][:] for i in range(r)]


def on_air():       # 공기청정기 순환
    global arr
    copy_arr = [arr[i][:] for i in range(r)]
    x, y = loc_air, 1       # 공기청정기 윗부분 위치
    copy_arr[x][y] = 0
    for i in [0, 3, 2, 1]:  # 우 상 좌 하
        nx = x + dx[i]
        ny = y + dy[i]
        while in_range(nx, ny) and arr[nx][ny] != -1:       # 배열을 넘어서거나, 공기청정기를 만나면 종료
            copy_arr[nx][ny] = arr[x][y]
            x, y = nx, ny       # 다음 위치로 이동
            nx += dx[i]
            ny += dy[i]

    x, y = loc_air + 1, 1   # 공기청정기 아래부분 위치
    copy_arr[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while in_range(nx, ny) and arr[nx][ny] != -1:       # 배열을 넘어서거나, 공기청정기를 만나면 종료
            copy_arr[nx][ny] = arr[x][y]
            x, y = nx, ny       # 다음 위치로 이동
            nx += dx[i]
            ny += dy[i]
    arr = [copy_arr[i][:] for i in range(r)]


r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]       # 미세먼지 상태
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]   # 우 하 좌 상

for i in range(r):
    if arr[i][0] == -1:
        loc_air = i # 공기청정기 윗부분 x 좌표
        break

for _ in range(t):  # t초 동안 확산과 공기청정기 순환
    spread()
    on_air()

dust = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            dust += arr[i][j]
print(dust)     # 미세먼지 양을 출력