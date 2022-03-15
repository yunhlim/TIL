from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1, -1, -1] for _ in range(n)] for _ in range(n)] # 방향마다 경우의 수를 적어준다. 오른쪽, 대각선, 아래

for i in range(n):
    for j in range(2):
        dp[i][j] = [0, 0, 0]    # 갈 수 없는 왼쪽부터 두 칼럼에 [0, 0, 0]을 넣어준다.

dp[0][1] = [1, 0, 0]        # 시작점, (0, 1)에서 오른쪽 방향
for i in range(2, n):       # 첫 번째 행에 값을 넣어준다.
    if arr[0][i]:
        dp[0][i] = [0, 0, 0]    # 중간에 0을 만나면 그 오른쪽은 다 0으로 처리
    else:
        dp[0][i] = dp[0][i - 1]

if arr[n-1][n-1] == 1:      # 벽이 n-1, n-1에 있는 경우
    dp[n-1][n-1] = [0, 0, 0]

queue = deque()
queue.append((1, 2))
while queue and dp[n-1][n-1][0] == -1:
    v = queue.popleft()
    y, x = v[0], v[1]

    if y == n or x == n or dp[y][x][0] != -1:   # 인덱스를 초과하거나 이미 확인한 값이면 보지 않는다.
        continue

    # 왼쪽에서 오른쪽 방향에서 왔을 때
    if arr[y][x-1]:    # 왼쪽에 벽이 있는 경우
        dp[y][x][0] = 0
    else:   # 왼쪽의 값 중 대각선, 오른쪽 방향으로 온 값을 더한다.
        dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][1] 
    # 대각선 방향으로 왔을 때
    if arr[y][x-1] or arr[y-1][x-1] or arr[y-1][x]: # 왼쪽, 대각선, 위쪽으로 벽이 있는 경우
        dp[y][x][1] = 0
    else:   # 왼쪽 위의 값 세 개를 다 더한다.
        dp[y][x][1] = sum(dp[y-1][x-1]) 
    # 위쪽에서 아래 방향으로 왔을 때
    if arr[y-1][x]:     # 위쪽에 벽이 있는 경우
        dp[y][x][2] = 0
    else:   # 위쪽의 값 중 대각선, 아래 방향으로 온 값을 더한다.
        dp[y][x][2] = dp[y-1][x][1] + dp[y-1][x][2] 

    queue.append((y, x + 1))
    queue.append((y + 1, x))
    queue.append((y + 1, x + 1))

if dp[n-1][n-1][0] == -1:   # 도착점에 도달하지 못한 경우 0 출력
    print(0)
else:
    print(sum(dp[n-1][n-1]))