def recur(floor, ho):
    if dp[floor][ho]:
        return dp[floor][ho]
    
    ans = 0
    for i in range(1, ho + 1):
        ans += recur(floor - 1, i)
    dp[floor][ho] = ans
    return ans

dp = [[0 for _ in range(15)] for _ in range(15)]
dp[0] = [i for i in range(15)]

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(recur(k, n))