from collections import deque


def shark(x, y, move):            # 아기 상어가 다음 먹이를 찾아 이동한다.
    global eat, size
    que = deque()
    que.append([x, y])
    visited = [[0] * n for _ in range(n)]       # 방문했는지 확인
    visited[x][y] = 1
    dist = 0            # 다음 먹이까지의 거리
    fishes = []         # 같은 거리인 경우 먹을 수 있는 물고기의 좌표들
    while que:
        dist += 1
        for _ in range(len(que)):
            x, y = que.popleft()     # 상어의 위치
            for i in range(4):       # 네 방향으로 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < n):   # 범위 안에 있는지 확인
                    continue
                if visited[nx][ny]:               # 확인했던 위치일 때
                    continue
                if 0 < arr[nx][ny] < size:      # 작은 물고기가 있을 때
                    fishes.append([nx, ny])
                elif arr[nx][ny] == 0 or arr[nx][ny] == size:       # 크기가 같은 물고기가 있거나, 물고기가 없을 때
                    que.append([nx, ny])
                    visited[nx][ny] = 1
        if fishes:
            fishes.sort()               # 물고기들 중 (맨 위 => 맨 왼쪽)에 있는 물고기 선택
            fish = fishes[0]
            eat += 1                    # 먹은 횟수 + 1
            if eat == size:             # 물고기를 먹은 개수가 크기랑 같아지면 진화
                size += 1
                eat = 0
            arr[fish[0]][fish[1]] = 0             # 먹은 물고기를 제거
            return shark(fish[0], fish[1], move + dist)
    return move


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size = 2        # 아기 상어 초기 사이즈 : 2
eat = 0         # 먹은 물고기 숫자 
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]       # 네 방향
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            print(shark(i, j, 0))