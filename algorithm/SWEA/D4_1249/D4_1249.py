from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[100000] * n for _ in range(n)]  # 나올 수 없는 아주 큰 값으로 초기화
    visited[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:   # 끝에 도달하면 continue
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y] + arr[nx][ny]:   # 더 작은 값일 때
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    queue.append((nx, ny))

    print(f'#{tc} {visited[n - 1][n - 1]}')