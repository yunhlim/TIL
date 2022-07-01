def recur(cur, visited):
    if cur < 0:                    # 다 일한 경우 종료
        return 0
    if dp[visited] != -1:           # 이미 확인한 경우
        return dp[visited]
    dp[visited] = INF
    for i in range(n):              # 일들을 순회
        if visited & (1 << i):      # 이미 했던 일인지 확인
            prv_visited = visited ^ (1 << i)
            dp[visited] = min(dp[visited], recur(cur - 1, prv_visited) + fee[cur][i])
    return dp[visited]

    
n = int(input())
fee = [list(map(int, input().split())) for _ in range(n)]          # 각 사람이 각각의 일을 할 수 있는 비용
INF = 10000 * n + 5
dp = [-1 for _ in range(1 << n)]     # 비용을 적을 DP

print(recur(n - 1, (1 << n) - 1))