# 탑다운 DP
# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

# def recur(cur):
#     if cur > n:
#         return -100000000 
#     if cur == n:
#         return 0

#     if dp[cur] != -1:
#         return dp[cur]

#     dp[cur] = max(recur(cur + 1), recur(cur + arr[cur][0]) + arr[cur][1])
#     return dp[cur]

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [-1 for _ in range(n)]
# print(recur(0))


# 바텀업 DP
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n)[::-1]:
    day, pay = arr[i]
    if day + i <= n:
        dp[i] = max(dp[day + i] + pay, dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])