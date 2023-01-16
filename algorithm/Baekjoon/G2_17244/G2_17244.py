from collections import deque


# 순열
def recur(cur, prv, time):
    global min_time
    if cur == len(destination) - 2:   # 물건을 다 찾은 경우
        min_time = min(min_time, time +
                       times[prv][len(destination) - 1])
        return

    for i in range(1, len(destination) - 1):
        if visited[i]:
            continue
        visited[i] = True
        recur(cur + 1, i, time + times[prv][i])
        visited[i] = False


# bfs로 각 point에서 각각 다른 point까지 걸리는 최소 시간 구하기
def bfs(node):
    arr_copy = [arr[i][:] for i in range(n)]
    que = deque()
    x, y = destination[node]
    que.append((x, y))
    arr_copy[x][y] = '#'

    d = 0
    while que:
        for _ in range(len(que)):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if arr_copy[nx][ny] != '#':
                    if arr_copy[nx][ny] == 'X':
                        times[node][stuff_num_find[(nx, ny)]] = d + 1
                    elif arr_copy[nx][ny] == 'S':
                        times[node][0] = d + 1
                    elif arr_copy[nx][ny] == 'E':
                        times[node][len(destination) - 1] = d + 1
                    que.append((nx, ny))
                    arr_copy[nx][ny] = '#'
        d += 1


m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]     # map 정보
stuff_cnt = 0                                  # 물건들 개수
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
INF = 1000000
min_time = INF
# 시작점 , 물건들, 도착점으로 정리 : 시작점의 key는 0, 물건들은 1 ~ 물건 개수, 도착점은 물건 개수 + 1
destination = {}
# 물건 좌표로 번호 찾기
stuff_num_find = {}

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            stuff_cnt += 1
            destination[stuff_cnt] = (i, j)
            stuff_num_find[(i, j)] = stuff_cnt
        elif arr[i][j] == 'S':
            destination[0] = (i, j)     # 시작점은 0
        elif arr[i][j] == 'E':
            end = (i, j)

destination[stuff_cnt + 1] = end        # 도착점은 물건 개수 + 1

times = [[0] * (len(destination))
         for _ in range(len(destination))]     # 각 point 간의 최소 소요 시간

for i in range(len(destination)):
    bfs(i)

visited = [0 for _ in range(stuff_cnt + 1)]    # 물건을 찾았는지 표시
recur(0, 0, 0)
print(min_time)
