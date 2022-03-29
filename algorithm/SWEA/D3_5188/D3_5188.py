def recur(x, y):    # 탑다운 DP
    if dp[x][y]:                    # 이미 계산했던 연산은 가져다가 사용한다.
        return dp[x][y]

    result = 1000                      # 비교할 최댓값
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:     # 최소값을 리턴
            result = min(result, arr[x][y] + recur(nx, ny))
    dp[x][y] = result          # 구한 값을 dp에 값을 넣어준다.
    return result


dx = [0, 1]     # 오른쪽, 아래
dy = [1, 0]
t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]    # 반복된 연산을 줄이기 위한 DP
    dp[n - 1][n - 1] = arr[n - 1][n - 1]    # 기저 조건
    print(f'#{tc} {recur(0, 0)}')