import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
INF = n * m
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = [[[INF, 2] for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((0, 0))
visited[0][0] = [1, 0]

while queue and visited[n-1][m-1][1] == 2:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < n and 0 <= nx < m):
            continue
        if arr[ny][nx] == 0:  
            if visited[y][x][1] < visited[ny][nx][1]:
                visited[ny][nx] = [visited[y][x][0] + 1, visited[y][x][1]]
                queue.append((ny, nx))
            elif visited[y][x][1] == visited[ny][nx][1]:
                if visited[y][x][0] + 1 < visited[ny][nx][0]:
                    visited[ny][nx] = [visited[y][x][0] + 1, visited[y][x][1]]
                    queue.append((ny, nx))
        else:
            if visited[y][x][1] == 0 and (visited[y][x][0] + 1 < visited[ny][nx][0]):
                visited[ny][nx] = [visited[y][x][0] + 1, 1]
                queue.append((ny, nx))

if visited[n-1][m-1][1] == 2:
    print(-1)
else:
    print(visited[n-1][m-1][0])