import sys
sys.setrecursionlimit(10**5)

def recur(cur):
    if cur == n:
        return 1
    if cur > n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    
    dp[cur] = recur(cur + 1) + recur(cur + 2)
    dp[cur] %= 10007
    return dp[cur]


n = int(input())
dp = [-1 for i in range(n)]
print(recur(0))