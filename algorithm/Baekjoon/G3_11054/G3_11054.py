n = int(input())
arr = [0] + list(map(int, input().split()))
m = max(arr)
dp_f = [[0] * (m + 1) for _ in range(n + 1)]    # 증가하는 방향
dp_b = [[0] * (m + 1) for _ in range(n + 1)]    # 감소하는 방향

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # dp 증가하는 방향
        if j == arr[i]:
            dp_f[i][j] = dp_f[i-1][j-1] + 1
        else:
            dp_f[i][j] = max(dp_f[i][j-1], dp_f[i-1][j])
        # dp 감소하는 방향
        if j == arr[-i]:
            dp_b[i][j] = dp_b[i-1][j-1] + 1
        else:
            dp_b[i][j] = max(dp_b[i][j-1], dp_b[i-1][j])

max_result = 0
for i in range(1, n + 1):
    max_result = max(max_result, dp_f[i][-1] + dp_b[-i][-1])

print(max_result - 1)