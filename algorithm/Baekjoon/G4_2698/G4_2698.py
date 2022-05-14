def recur(cur, cnt, prv):
    if cur == 0 or cnt < 0 or cur <= cnt:
        return 0
    if dp[cur][cnt][prv] != -1:
        return dp[cur][cnt][prv]
    if prv == 1:
        ret = recur(cur - 1, cnt, 0) + recur(cur - 1, cnt - 1, 1)
    else:
        ret = recur(cur - 1, cnt, 0) + recur(cur - 1, cnt, 1)
    dp[cur][cnt][prv] = ret
    return ret

t = int(input())
dp = [[[-1, -1] for _ in range(101)] for _ in range(101)]

dp[1][0][1] = 1
dp[1][0][0] = 1

for _ in range(t):
    n, k = map(int, input().split())
    print(recur(n, k, 0) + recur(n, k, 1))