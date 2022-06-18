def in_range(x, y):     # 체스판 범위 안인지 확인
    return 0 <= x < n and 0 <= y < n


def check(x, y):        # 대각선에 비숍있는지 체크
    for i in range(2):      # 왼쪽 위, 오른쪽 위 대각선 체크
        nx = x + dx[i]
        ny = y + dy[i]
        while in_range(nx, ny):    # 체스판 범위 안인 경우
            if visited[nx][ny]:     # 대각선에 비숍이 놓여 있는 경우 False
                return False
            nx += dx[i]
            ny += dy[i]
    return True             # 대각선에 비숍이 없는 경우 True


def recur(x, y, cnt):   # 2칸씩 건너띄며 확인
    color = (x + y) % 2     # 현재 칸의 색
    if not in_range(x, y):       # 다 확인한 경우
        result[color] = max(result[color], cnt)      # 최댓값 갱신
        return
    if (n * n - 1 - (x * n + y)) // 2 + 1 + cnt <= result[color]:   # 남은 칸에 다 비숍을 놔도 최대값을 바꾸지 못하는 경우
        return

    # 다음 같은 색의 좌표 값 구하기
    ny = y + 2
    nx = x + ny // n
    if ny >= n:      # 다음 행으로 이동
        if n % 2:       # 체스판의 크기 n이 홀수인 경우
            ny %= n
        else:           # 체스판의 크기 n이 짝수인 경우
            ny = 0 if ny % 2 else 1

    if arr[x][y] and check(x, y):   # 비숍을 놓을 수 있을 때
        visited[x][y] = 1
        recur(nx, ny, cnt + 1)
        visited[x][y] = 0
    recur(nx, ny, cnt)              # 비숍을 놓지 않을 때


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]       # 비숍을 놓을 수 있는 칸이 입력으로 주어진다.

visited = [[0] * n for _ in range(n)]
dx, dy = [-1, -1], [-1, 1]  # 왼쪽 위, 오른쪽 위
result = [0, 0]     # 칸이 흰색인 경우와 검정인 경우 나눠서 구한다.
recur(0, 0, 0)      # 칸이 검정인 경우
recur(0, 1, 0)      # 칸이 흰색인 경우
print(sum(result))      # 칸이 흰색 검정인 경우의 값을 더한다.