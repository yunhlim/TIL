from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 1, 0, -1]  # 우 하 좌 상
dx = [1, 0, -1, 0]
queue = deque()
day = 0

for i in range(n):  # 큐에 1을 담는다.
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()
    for i in range(4):  # 값의 네 방향으로 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0:    # 범위를 넘지않으며 0이면 값을 바꾼다.
            arr[ny][nx] = arr[y][x] + 1     # 현재 가운데 값에 1을 더해준다. 익으면 날짜가 +1
            if arr[ny][nx] - 1 > day:       # 0일일 때 값이 1, 1일일 때 값이 2이니 1을 빼준 값을 넣어준다.
                day = arr[ny][nx] - 1
            queue.append((ny, nx))          # 영역을 확장하면 그 부분도 다시 큐에 담는다.

for ar in arr:      # 2차원 배열을 읽으며 0이 있는지 확인한다.
    if 0 in ar:
        day = -1    # 0이 있으면 아직 익지 못한 토마토가 있으니 -1을 출력한다.

print(day)