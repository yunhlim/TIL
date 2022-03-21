from collections import deque


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
INF = n * m
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[[INF, 2] for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((0, 0))
visited[0][0] = [1, 0]

while queue and visited[n-1][m-1][0] == INF:
    y, x = queue.popleft()
    print(y, x)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < n and 0 <= nx < m):
            continue
        if arr[ny][nx] == 0:
            print(ny, nx)   
            if visited[y][x][1] < visited[ny][nx][1]:
                visited[ny][nx] = [visited[y][x][0] + 1, 0]
                queue.append((ny, nx))
            elif visited[y][x][1] == visited[ny][nx][1]:
                if visited[y][x][0] + 1 < visited[ny][nx][0]:
                    visited[ny][nx] = [visited[y][x][0] + 1, visited[y][x][1]]
                    queue.append((ny, nx))
        else:
            if visited[y][x][1] == 0:
                if visited[y][x][0] + 1 < visited[ny][nx][0]:
                    visited[ny][nx] = [visited[y][x][0] + 1, 1]
                    queue.append((ny, nx))
print(visited)
print(visited[n-1][m-1])