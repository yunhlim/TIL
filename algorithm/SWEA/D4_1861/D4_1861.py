from collections import deque


def check(y, x):    # 현재 위치에서 최대 이동 횟수를 찾는다.
    cnt = 1     # 이동 횟수, default가 1
    num = arr[y][x]
    queue = deque()
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):  # 4방향 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n: 
                if abs(arr[ny][nx] - arr[y][x]) == 1:    # 1 크거나 같은 경우
                    if arr[ny][nx] - arr[y][x] == -1: # 1 더 작은 경우
                        num = arr[ny][nx]             # 시작점 변경
                    cnt += 1
                    queue.append([ny, nx])
        arr[y][x] = -1
    return cnt, num


t = int(input())
dy = [0, 1, 0, -1]  # 우 하 좌 상
dx = [1, 0, -1, 0]
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    room = 0        # 방 번호
    max_cnt = 0     # 이동 횟수
    for i in range(n):
        for j in range(n):
            if arr[i][j] != -1:
                cnt, num = check(i, j)
                if cnt > max_cnt or (cnt == max_cnt and num < room):
                    room = num
                    max_cnt = cnt
                
    print(f'#{tc}', room, max_cnt)