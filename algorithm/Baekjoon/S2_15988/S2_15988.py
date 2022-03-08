T = int(input())
dp = [0 for _ in range(1000005)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
s = 4
for i in range(T):
    n = int(input())
    while s <= n:
        for i in range(1, 4):
            dp[s] += dp[s - i]
            dp[s] %= 1000000009
        s += 1
    print(dp[n])