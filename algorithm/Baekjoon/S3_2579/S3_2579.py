def recur(cur, prv):    # 현재 계단과 이전 계단 밟았는지 여부
    if cur < 0:         # 계단의 범위를 넘어서는 경우
        return 0

    if dp[cur][prv]:    # 값이 존재하는 경우
        return dp[cur][prv]
    
    if prv == True:     # 이전 계단을 밟은 경우
        dp[cur][prv] = recur(cur - 1, False) + arr[cur]
    else:               # 이전 계단을 밟지 않은 경우
        dp[cur][prv] = max(recur(cur - 2, True), recur(cur - 2, False)) + arr[cur]
    return dp[cur][prv]

n = int(input())        # 계단의 개수
arr = [0 for _ in range(n)]         # 계단의 점수
for i in range(n):
    arr[i] = int(input())
dp = [[0, 0] for _ in range(n)]     # 연속해서 계단을 밟지않은 경우의 점수, 연속해서 밟은 경우의 점수 두 가지 상태 표시
print(max(recur(n - 1, False), recur(n - 1, True)))