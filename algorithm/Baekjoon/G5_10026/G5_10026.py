import sys
sys.setrecursionlimit(10000)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, color):       # 적록색약이 아닌 경우 인접리스트 구하기
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny] and color == arr[nx][ny]:
            dfs(nx, ny, color)


def dfs_rg(x, y, color):    # 적록색약인 경우 인접리스트 구하기
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and not visited[nx][ny]:
            if color == 'B' and arr[nx][ny] == 'B':
                dfs_rg(nx, ny, color)
            elif color != 'B' and arr[nx][ny] != 'B':
                dfs_rg(nx, ny, color)


n = int(input())
arr = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 적록 색약이 아닌 경우
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        dfs(i, j, arr[i][j])
        cnt += 1

# 적록 색약인 경우
visited = [[0] * n for _ in range(n)]
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        dfs_rg(i, j, arr[i][j])
        cnt_rg += 1

print(cnt, cnt_rg)