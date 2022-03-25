def recur(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    ret = 0
    if dp[x][y] != -1:
        ret = dp[x][y]
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
                ret += recur(nx, ny)
        dp[x][y] = ret
    return ret


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dp = [[-1] * n for _ in range(m)]

print(recur(0, 0))