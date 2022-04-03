from collections import deque


def in_degree(x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
s_x, s_y = map(lambda x: int(x) - 1, input().split())
e_x, e_y = map(lambda x: int(x) - 1, input().split())
# 폰이 있는 경우는 1, 없는 경우는 0
arr = [input() for _ in range(n)]
INF = 10000000
visited = [[INF] * n for _ in range(n)]         # 이미 그려진 걸 확인하는 과정을 생략하기 위함!!
dx = [1, 1, -1, -1]     # 대각선 방향으로 이동
dy = [1, -1, 1, -1]

que = deque()
que.append((s_x, s_y))
visited[s_x][s_y] = 0       # 비숍 방문 표시

while que:
    x, y = que.popleft()
    if x == e_x and y == e_y:
        print(visited[x][y])
        exit()
    for nxt in range(4):
        nx = x + dx[nxt]
        ny = y + dy[nxt]
        # 배열의 크기를 벗어나거나, 폰이 있거나, 그 위치부터 다른 정점이 이미 파악한 경우(중복 확인 제거)
        while in_degree(nx, ny) and arr[nx][ny] == '.' and visited[nx][ny] >= visited[x][y] + 1:
            if visited[nx][ny] == INF:        # 비숍이 없던 경우만
                visited[nx][ny] = visited[x][y] + 1         # 비숍 방문 표시
                que.append((nx, ny))
            nx += dx[nxt]
            ny += dy[nxt]

print(-1)