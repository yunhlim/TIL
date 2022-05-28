from collections import deque


def bfs(a, b):
    que = deque()
    que.append([a, b])
    arr[a][b] = 0
    cnt = 0
    while que:
        cnt += 1
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                arr[nx][ny] = 0
                que.append([nx, ny])
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = []

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])