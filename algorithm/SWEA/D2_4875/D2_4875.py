# 미로
def miro():
    while stack:
        y, x = stack.pop()
        arr[y][x] = -1      # 지나간 길 표시
        for i in range(4):  # 네 방향 탐색
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 3:    # 도착점 찾으면 1 return
                    return 1
                elif arr[ni][nj] == 0:  # 갈 수 있는 곳을 전부 stack에 담는다.
                    stack.append((ni, nj))
    return 0    # 도착점 못 찾으면 0 return

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]   # 미로
    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작점 찾기
                stack = [(i, j)]
                break
    print(f'#{tc} {miro()}')