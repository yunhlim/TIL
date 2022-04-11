def recur(cur):
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] =  not (recur(cur - 1) and recur(cur - 3) and recur(cur - 4))
    return dp[cur]


n = int(input())
dp = [-1 for _ in range(n + 4)]
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1
if recur(n):
    print('SK')
else:
    print('CY')