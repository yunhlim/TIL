def in_range(x, y):
    return 0 <= x < h and 0 <= y < w


def check(x, y):
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    cnt = 1     # 현재 타일 주변(대각선 포함) 타일 개수 확인
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and arr[nx][ny] == "*":
            cnt += 1

    if cnt == 3:
        return True
    else:
        return False


def dfs(x, y, dir_arr):      # 인접한 타일 개수 파악(대각선 X)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 1
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and arr[nx][ny] == "*" and not visited[nx][ny]:
            if i in dir_arr:        # 이미 나온 방향이 또 나온 경우는 잘못된 값인 4를 리턴
                return 4
            dir_arr.append(i)
            cnt += dfs(nx, ny, dir_arr)
    return cnt


def sol():
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                if not visited[i][j]:
                    if dfs(i, j, []) != 3:
                        return 'NO'
                if not check(i, j):
                    return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    print(sol())
