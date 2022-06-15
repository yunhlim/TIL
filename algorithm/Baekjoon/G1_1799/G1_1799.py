def recur(x, y, cnt):
    # 가지치기
    if 2 * n - 1 - (x + y) + cnt <= max_cnt:     # 앞으로 비숍으로 다 채워도 현재 구한 최대값보다 작거나 같은 경우
        return
    while not arr[x][y] or visited[x-min(x, y)][y-min(x, y)]:
        if x == 0:      # 현재 대각선을 다 확인한 경우
            x = y + 1
            y = 0
        else:           # 오른쪽 위로 이동
            x -= 1
            y += 1
        if y == n:
            y = 0
            x += 1
        if x == n:      # 놓을 수 있는 자리를 다 확인한 경우
            max_cnt = max(max_cnt, cnt)
            return

   # 비숍을 놓을 수 있는지 확인
        visited[x][y] = 1
        recur(cur + 1, cnt + 1)        # 비숍을 놓는 경우
        visited[x][y] = 0
    
    recur(cur + 1, cnt)    # 비숍을 놓지 않는 경우
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
dx = [-1, -1] # 오른쪽 위, 왼쪽 위 순서
dy = [1, -1]
max_cnt = 0
recur(0, 0, 0)
print(max_cnt)