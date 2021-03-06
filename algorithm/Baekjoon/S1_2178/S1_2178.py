from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
que = deque()
que.append([0, 0])
visited[0][0] = 1

cnt = 1
while que:
    sz = len(que)
    for _ in range(sz):
        x, y = que.popleft()
        if x == n - 1 and y == m - 1:
            print(cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and arr[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append([nx, ny])
    cnt += 1