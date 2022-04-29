t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    for i in range(0, n):
        dp[0][i] = arr[0][i] + max(dp[1][i - 1] if i >= 1 else 0, dp[1][i - 2] if i >= 2 else 0)
        dp[1][i] = arr[1][i] + max(dp[0][i - 1] if i >= 1 else 0, dp[0][i - 2] if i >= 2 else 0)

    print(max(dp[0][n - 1], dp[1][n - 1]))