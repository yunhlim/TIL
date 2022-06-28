from collections import deque


def open(door):        # 열 수 있는 key가 있는지 확인
    if chr(ord(door) + 32) in keys:
        return True
    else:
        return False


def bfs(x, y):          # 현재 노드 주위를 탐색
    que = deque()
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for nxt in range(4):
            nx = x + dx[nxt]
            ny = y + dy[nxt]
            if 0 <= nx < h and 0 <= ny < w and go(nx, ny):
                que.append([nx, ny])


def go(x, y):       # 갈 수 있으면 가고 True 리턴, 아니면 안 가고 False 리턴
    global cnt
    if visited[x][y]:                   # 이미 방문했으면 갈 수 없다.
        return False
    elif arr[x][y] == '.':                # 빈 공간을 만나면 갈 수 있다.
        visited[x][y] = 1
        return True
    elif arr[x][y] == '*':              # 벽을 만나면 갈 수 없다.
        return False
    elif 'a' <= arr[x][y] <= 'z':       # 열쇠를 주웠을 때
        keys.append(arr[x][y])          # 열쇠 추가
        visited[x][y] = 1
        return True
    elif 'A' <= arr[x][y] <= 'Z':       # 문을 마주쳤을 때
        if open(arr[x][y]):             # 열 수 있는지 확인
            visited[x][y] = 1
            return True
        else:
            doors.append([x, y])     # 열 수 없으면 열지 못한 문에 추가
            return False
    else:
        cnt += 1                        # 문서를 만났을 때 + 1
        visited[x][y] = 1               # 방문 표시
        return True


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n = int(input())
for _ in range(n):
    h, w = map(int, input().split())    # 지도의 높이 h, 너비 w
    arr = [input() for _ in range(h)]   # 지도
    keys = list(input())                # 소지하고 있는 키들
    doors = deque()      # 열지 못한 문의 좌표를 큐에 담는다 : [x, y]
    visited = [[0] * w for _ in range(h)]   # 방문 표시
    cnt = 0     # 획득한 문서의 수

    # 건물 가장자리 탐색
    for i in range(h):
        if i == 0 or i == h - 1:    # 첫 행과 마지막 행은 전부 다 탐색
            for j in range(w):
                if go(i, j):
                    bfs(i, j)
        else:                       # 나머지 행은 양 끝만 탐색
            if go(i, 0):
                bfs(i, 0)
            if go(i, w - 1):
                bfs(i, w - 1)

    while doors:                    # 열지 못했던 문들을 탐색
        change = 0
        sz = len(doors)
        for _ in range(sz):
            x, y = doors.popleft()
            if go(x, y):            # 문을 열 수 있는지 확인하고 이동
                bfs(x, y)
                change = 1
            else:
                doors.append([x, y])
        if not change:              # 더 열었던 문이 있을 때만!
            break

    print(cnt)