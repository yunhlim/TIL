def recur(a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    
    ret = 2 ** 31
    for i in range(a, b):
        ret = min(ret, recur(a, i) + recur(i + 1, b) + arr[a][0] * arr[i][1] * arr[b][1])
    dp[a][b] = ret
    return ret


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]   # [a, b] 까지 중 곱셈 연산 횟수의 최솟값
for i in range(n):  # [i, i]는 행렬이 하나이므로 0이다.
    dp[i][i] = 0
print(recur(0, n - 1))