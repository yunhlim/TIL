def in_range(x, y):     # 범위 안에 있는지 확인
    return 0 <= x < n and 0 <= y < m

def check():        # 외부 공기와 맞닿은 부분이 2개 이상인 치즈 제거
    remove = []
    for x in range(n):
        for y in range(m):
            if arr[x][y]:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if air[nx][ny]:     # 외부 공기와 맞닿은지 확인
                        cnt += 1
                if cnt >= 2:            # 2면 이상 맞닿은 경우
                    remove.append([x, y])
    return remove


def add_air(x, y):  # 외부 공기의 연결요소들을 이어준다. DFS로 확인
    air[x][y] = True
    
    for i in range(4):      # 네 방향으로 확장
        nx = x + dx[i]
        ny = y + dy[i]
        # 공기가 아니면 확장 X
        if not in_range(nx, ny) or air[nx][ny] or arr[nx][ny]:
            continue
        add_air(nx, ny)
    

def cheese():
    add_air(0, 0)       # 처음 외부 공기들을 연결
    day = 0
    while True:
        remove = check()
        if not remove:          # 더 이상 제거할 치즈가 없으면 종료
            return day
        for x, y in remove:
            arr[x][y] = 0       # 치즈 제거
            add_air(x, y)       # 외부 공기 유입
        day += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
air = [[0] * m for _ in range(n)]       # 외부 공기는 1, 아니면 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(cheese())