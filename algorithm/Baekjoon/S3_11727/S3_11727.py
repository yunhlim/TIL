def recur(cur):
    if cur == 1:
        return 1
    elif cur == 2:
        return 3

    if dp[cur]:
        return dp[cur]
    dp[cur] = recur(cur - 2) * 2 + recur(cur - 1)
    dp[cur] %= 10007
    return dp[cur]



n = int(input())
dp = [0 for _ in range(n + 5)]
print(recur(n))